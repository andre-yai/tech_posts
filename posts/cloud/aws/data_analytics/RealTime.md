RealTime - Immediate Actions
- Kinesis Data Stream (KDS)
- Simple Queue Service (SQS)
- Internet of Things (IoT)


# Kinesis Data Stream (KDS)
- *Producer* : Aplication, Client, SDK, KPL, Kinesis Agent.
- Send records: Partition Key, Data Blob (up to 1MB) 
        - Sending 1 MB/sec or 1000 msg/sec per shard.
- Made of shards (1 to N)
- Receive record: Partition Key, Sequence no. , Data Blob.
- *Consumer*: Kinesis Client Library, Kinesis SDK 
- Consumers AWS Services: Lambda, Kinesis Data Firehouse, Kinesis Data Analytics.
- Data Retention: 1 to 365 days.
- Ability to reprocess (replay) data.
- Immutability: Once inserted cannot be deleted.
- Data that shares same partition goes to same shard (ordering).

## Capacity Modes:

Provision Mode
- Choose number of shards provisioned, scale manualy or using API.
- Each shard gets:
        - 1 MB/s in
        - 2 MB/s out
- You pay per shard provisined per hour.

On-demand mode
- No need to provision
- Default capacity provisioned (4 MB/s or 4000 records per second)
- Scales automatically based on observed throughput peak during las 30 daus
- Pay per stream per hour & data in/out per GB.

- Control access / authorization using IAM polices
- In Flight using HTTPS
- At rest using KMS
- Can build an encrypt/decript on client side (harder)
- Monitor API calls using CloudTrail

## *Producer* : SDK, KPL, Kinesis Agent.
- SDK, KPL, Kinesis Agent and 3rd libraries.

- Send records: Partition Key, Data Blob (up to 1MB) 
        - Sending 1 MB/sec or 1000 msg/sec per shard.
- Made of shards (1 to N)
- Receive record: Partition Key, Sequence no. , Data Blob.
## SDK:
- APIs are used PutRecord (one) and PutRecords(many records)
- *PutRecords*: Uses Batching and increases throughput.
- Use *ProvisionedThroughputExceeded* if we go over the limits
- Managed AWS Sources for Data Stream: Cloud Watch, IoT, Data Analytics.

### Exceptions
- ProvisinedThroughputExceeded Exceptions
- When sending more data (excedding MB/s or TPS)
- Make sure you don't have a hot shard.

## KPL
- Easy to use in C++/Java
- High Performance long-running producers
- Automatic and Configurable Retry.
- Syncronous or Asyncronous API. (better performance for async)
- Submit metrics to CloudWatch for monitoring
- Batching - on by default - increase throughput, decrease cost:
- Collect records and write to multiple shards.
  - Aggregate
- Compression must be implemented by user.
- KPL Records must be de-coded with KCL.

### *RecordMaxBufferedTime*

Aggregate into One Record < 1MB
if more use PutRecords.
- RecordMaxBufferedTime (default 100ms)
- KPL can infur processing delay. 
- Lager RecordMaxBufferedTime better efficiencie and better performance
- No use if does not support delay. USE SDK INSTEAD.

## Kinesis Agent
- Monitor Logs Files and send them to Kinesis Data Stream. 
- Java based agent on top of KPL
- Install on Linux environment,
- Write from multiples directories and write to muiltiple streams.
- Routing feature based on directory/ log file.
- Pre-process data before sending to stream.
- Handle file rotation, checkpointing and retry.
- Emist metric to CloudWatch for monitoring.

# Kinesis Consumers
- Kinesis SDK, Kinesis Client Library, Kinesis Connector Library.
- 3rd party: Spark, Log4j, Appenders. Flume, Kafka Connec.
- Kinesis Firehouse.
- AWS Lambda.
- Kinesis Enhanced Fan Out.

# SDK.
Classic Kinesis - polled by consumers from a shard.
- Each shard has 2MB total aggerate throughput.
- GetRecords returns up to 10MB of data (then thorttle for 5 seconds) or up to 1000 records.
- Max 5 GetRecords API calls per shard per second = 200ms latency.
- If 5 consumers appplication consume form the same shard, every consumer can poll once a second and receive less 400 KB/s. 
2MB/5s = 400 KB/s.

## KCL
- Java first (GO, Python, Net, JS)
- Read records from Kinesis produced with the KPL (de-aggregation)
- Shared Discovery: share multiples shards with multiple consumers in one group.
- Checkpount feature to resume progress.
- Leverages DynamoDB for coordination and checkpointing (one row per shard)
- Make sure has enough WCU/RCU. 
- Or use On-Demand for DynamoDB.
- Otherwise DynamoDB may slow down KCL.
- Records processors will process the data
- ExpiredInteratorException => increase WCU

## Kinesis Connector Library.
- Needs to run on EC2.
- Java, Leverages KCL
- Write data to S3, DynamoDB, Redshift, ElasticSearch.
- Kinesis Firehouse replaces the Connector Library.

## Lambda.
- Can read records from Kinesis Data Stream.
- Lambda consumer has a library to de-aggregate record from the KPL.
- Lambda can be used to run lightweight ETL to:
S3, DynamoDB, Redshift, ElasticSearch, Anywhere you want.
- Can be used to trigger notifications/ send emails in real time.
- Configurable batch size.


## Kinessi Enhanced Fun Out
- New Aug 2018
- Works on KCL 2.0
- Each consumers get 2MB/s of provisioned throughput per shard.
- 20 consumer will get 40MB/s per shard aggregated.
- No more 2 MB/s limt per shard.
- Pushes data form HTTP/2
- Reduce latency (~70 ms)

### When to use it.
- Standard mode:
- Low number of consumer applications
- Can tolerate ~200ms latency.
- Minimize cost.

- Enhance
- Multiple Consumer applications for same Shard.
- Low latency ~70ms
- Higher Cost.
- Default 5 consumers using enhance fan-out per data stream.

## Scaling
### Adding Shards.
- Shard Splitting. 
- Splits a "hot shard" partition.
- Can be used to increase the Stream capacity.
- The old shard is closed and will be delited once is expired.

### Removing Shards.
- Merge Shards
- Old shards are closed and deleted based on data expiration.

- Out-of-records.
- After resharding, can read from child shards.
- If you start reading the child before completing reading the parent, you could read data from a particular hash key out of order.
- After a reshard, read entirely from the parent until you don't have new records.
- KCL has this logic already built in.

# Auto Scaling
- Not native in Kinesis.
- API Call: UpdateShardCount
- Auto Scaling with Lambda.
- Cannot do  resharding in parallel. Plan capacity in advance.
- Only one resharding operation at a time.
- 1000 shards, it takes 30K seconds.


## Handle Duplicate Records.
Producers.
- Producer retries can create duplicates due to network timeouts.
- Embed unique record ID on consumer side.
Consumer side:
- Retry to read.
- Restart: 
-  a worker terminates unexpected
-  shards are merged or split
-  application is deployed.
- Fixes: 
- Must be on cosumer application.

# Security
- Access and auth IAM
- HTPS
- KMS
- Encrypting on Client
- VPC endpoints.

# Stream Cloud Watch Logs.
- Using Logs Subscriptions Filters.
- Data Stream : if you want to do real time analytics.
- Firehouse : if you want to near real time convert or store in S3, Redshift, elaticSearch
- Lambda: if you want to real time load.
