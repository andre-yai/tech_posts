# Amazon OpenSearch.
- Search and visualizations
- Faster than Apache Spark for certain applications.
- A for of Elasticsearch and Kibana
- A search engine
- Scalable version of Lucines
- Visualization tool (Dashboards = Kibana).
- Data Pipeline: Kinesis replaces Beats & LogStash.
- OpenSearch application: full-text search, log analytics, application monitoring, security analytics, clickstream analytics.
- Documents.  - Storage and retrive. Also JSON documents
- Types - schemas and mapping shared by documents. Like schema
- Index - powers search into all documents.
- Index split into shards. Self-contained Lucenes.
- Write request are routed to the primary shard, then replicated.
- Read requests - are routed to the primary or replica shards.

- Fully-managed (but not serverless)
- Scale up or down without downtime. Not automatic
- Pay what you use. Instance-hours, storage, data transfers
- Network isolation. IOT
- AWS integrations.
    - S3 buckets. Kinesis Data Streams, DynamoDB Sreams.
    - CloudWatch/CloudTrail
    - Zone awareness
- OpenSearch 
    - Dedicated master node(s)
        - Count and instance types.
    - Domains
    - Snapshots to S3.
    - Zone Awareness
- Security
    - Resource-based policies
    - Identity based polices
    - Ip-based polices
    - Request siging
    - VPC : decide at first
    - Cognito: view dashboard
- Getting inside a VPC from outside.
- Nginx reverse proxy on EC2 forwarding to ES domain
- SSH tunnel for port 5601
- VPC Direct Connect
- VPN
- Anti-pattern
    - OLTP: Use RDS or DynamoDB
    - Ad-hoc data query: Athena
- Use OpenSearch for search and analytics.

- Cold/Warm/Ultrawarm/hot storage
- Standard data nodes use "hot" storage. Instant Stores or EBS volumes
- UltraWarm storage uses S3 + caching: Few writes. Slower performance but much lower cost. Must have a dediceted master node.
- Cold Storage: S3. Even cheaper. Periodic reseach or forensic analysis .Must gave dedicated master and have UltraWarm enable too. T2 or T3 instances. Fine-grained access control, must map users to cold_manager role in OpenSearch Dashboard.

# Index State Management

- Automates index management polices
- Delete old instances after a period of time. Read only state after a period of time.
- Move indeces from hot -> UltraWarm -> cold.
- Reduce replica
- Automate index snapshors
- Schedule run
- Rollups -> summarized indeces.
- Index transforms -> group and different view to analyze data.
- Cross-cluster. -> replicate and high availability. 
- Reduce data georgraphically for better latency.
- "Follower" index pulls data from "leader" index.
- Fine-grained access control and node-to-node encryption.
- Remote reindex 

# Stability
- 3 dedicated master nodes. Avoids "split brain".
- Don't run out of disk spaces. SourceData * (1 + Number of Replicas) * 1.45 (overhead)
- Choosing the number of shards.
    - (Source data + grow) * (1 + index overhead_metadata) / desired shard size.
    - Limit number of shards per node
- Instance types:
    - At least 3 node
    - Mostly about storage requirments.

# Performance
- Shards allocations.
- Too many shards in cluster.
- JVMMemoryPressurece - delete old unused indices

