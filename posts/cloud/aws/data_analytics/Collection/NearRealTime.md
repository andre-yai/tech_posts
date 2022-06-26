Near-real time - Reactive actions
- Kinesis Data Firehouse (KDF)
- Database Migration Service (DMS)

# Kinesis Data Firehouse.
- Read from client, SDK, KPL, Kinesis Agent
- Transform data in Lambda.
- Sends to:
    - AWS. S3, Redshift, ElasticSearch
    - HTTP Endpoint
    - Open: Splunk, Datadog, MongoDb, etc
- Failure goes to S3 bucket.
- Full Managed Service, no administration
- Near Real Time, (60s latency)
- Load data into Redshift, S3, ElasticSearch, Splunk,
- Automatic scaling 
- Support many data format.
- Convert data from JSON to Parquet/ ORC. Only for S3.
- Data Transformation through Lambda (CSV, JSON)
- Supports compression when target to S3.
- Only GZip is loaded to Redshift.
- Pay for amount going to Firehouse.
- Spark/ KCL nor read from Firehouse.
- No  data storage.

## Buffer Size.
- Accumulates data in a buffer.
- Can be flushed based on time and size.
- Size (ex: 32MB): is reached, it's flushed.
- Time (ex: 2min): if is reached, it's flushed.
- Can automaticaly increase buffer size.
- Min 1min.
