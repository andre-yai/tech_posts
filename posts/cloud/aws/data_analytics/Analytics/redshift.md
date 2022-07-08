# Amazon Redshift
- Fully Managed, petabyte scale data warehouse.

- Fully managed, petabyte scale data warehouse service. 10x better performance than other DW's
- OLAP not OLTP
- Cost effective
- Sql, ODBC, JDBC interfaces.
- Scale up and down on demand
- Built-in replication & backups
- Monitoring via CloudWatch/CloudTrail. 
- Accelarate analytics workloads. Unified data warehouse & data lake.
- Mordern Data Warehouse
- Stocks trade , gaming, social.
- Clusters.
    - Leader node - Client and compute interface
    - Compute node. - Executing commands and send to leader to aggregate. Dense for large operations.

# Redshift Spectrum
- Query exabytes of unstructed data in S3 without loading.
- Limitless concurrency
- Horizontal scaling
- Separe storage & compute resources
- Wide variety of data formats
- Support of Gzip and Snappy Compression
- Redshipt perfomance : Massivel Parallel Processing (MPP), columnar data storage , column compressions. Storage space and query performance.

# Durability
- 3 copies: Original, Replication, Backup in S3
- Replication within cluster
- Backup to S3. - Replicated to another region
- Automated snapshots
- Failed drives / nodes automatically replaced
- However - limited to a single availability zone (AZ)

# Scaling  Redshift
- Vertical (instance type) and horizontal (number of nodes) scaling on demand
- During scaling: A new cluster is created while your old one remains available.
- CNAME is flipped to new cluster
- Data moved in parallel to new compute nodes.

# Distribution Sytles
- Distribute data uniformaly and decrease number of data flow.
- AUTO: size of table data.
- EVEN: spread equal circular manner.  Not to Join
- KEY: matching key values in one column. Queries on a specific column in your data.
- ALL: Entiery table distributed to every node. Takes a lot of time to locate or insert data into multiple tables. Apropriate for data that is not updated frequently or extensively. Not for small data. Query PGCLASS INFO VIEW to view distribution style.

# Sort Keys
- Stored on disk in sorted order based on column you designate as sort key.
- Like an index.
- Makes for fast range queries.
- Chossing a sort key. Recency, Filtering and Joins
- Single vs Compound vs Interleaved sort keys.
- Single: Value, data and order
- Compond: Compound key. Compression. Default 
- Interlead: Multiple keys for filter.

# Importing/Exporting Data
- COPY command
    - Importing
    - Parallelized efficient
    - From S3, EMR, DynamoDB, remote hosts
    - S3 requires a manifest file and IAM role
    - Load large amount of data from outside
    - External data
    - If inside : Select or Create table as
    - Decript data - Hardware-accelareted SSL
    - Gzip, Lzop and bzip2 compression
    - Automati compression option
    - Narrow tables (lots of rows, few columns)
        Load wit a single Copy. Use few copy commands
    - Cross-regions: KMS encreypted Redshift cluster and Snapshot of it.
    - Across to another region.
    - DBLink: Connect Redshift to PostgreSQL. Copy and sync.
- UNLOAD command
    - Export data
    - To files in S3 
- Enhanced VPC routing : faster export and importing data.

# Integrations
- S3
- DynamoDB
- EMR/EC2
- Data Pipeline
- Database Migration Service

# Workload Management (WLM)
- Prioritize short, fast queries vs long, slow queries.
- Query queues
- Via console, CLI or API

# Concurrency Scaling
- Adds cluster capacity to handlw increase in concurrent read queries.
- Support virtually unlimited concurrent user & queries.
- WLM queues manage with queries are sent.

# Automatic Workload Management
- creates up to 8 queues.
- Default 5 queues with even memory allocation
- Large queries -> concurrency lowered.
- Small queres 
- Config: Priority, scaling mode, user groups, query groups, query monitoring rules. 

# Manual
- One default queues 
- Superuser queue with concurrnecy level 1
- Define up to 8 queues.
- Time out. Queues hoping

# Short Query Acceleration
- Priortigze short-running queries over longer-running ones.
- Can be use in place of WLM 
- Use machine learning to predict time.

# VACCUTM
- Recovers space from deleted rows and sort order
- FULL : default. Resort and reclaim store
- Delete only: reclaim store
- Sort only: resort 
- Reindex: resort key

# ANTI PATTERN
- Small data sets : RDS
- OLTP : RDS or DynamoDB
- Unstructered data : ETL first EMR or Glue
- BLOB : large binary files. Use S3.

# Elastic Resize
- Quickly add or remove nodes of same type
- Cluster is down 
- Doble or halving 

# Classic resize
- Node type

# Snaphot, restore, resize
- Copy and resize new cluster
- Then shift later.

# New
- RA3 nodes with managed storage. Optmized to Redshift. SSD based.
- Resdsihft data lake export: unload to S3 in Parquet. Partioned siported EMR, Athena, Glue
- AQUA: Advance Query Accelartion. Layer S3 and Redshift. Closer to S3. 10x faster. 

# Security Concernt
- Hardware Security Module (HSM).
- Must use a cliend and server certificate to configure a trusted connection between Redshift and HSM.
- Migrating to HSM. Must create first the new encrypted cluster and then mode data to it.

- Access and privileges for user or group:
- Use GRANT or REVOKE commands in SQL
- Grant select on table fooo to bob.

# Redshift Serverless
- Automatic scaling and provising for your workload.
- Optimize costs & performance
- Use ML to maintain performance across variable & sporadic workloads
- Spinup of development
- Ad hoc
- Need an IAM role with certain policy
- Database name
- User credentials
-  VP
- Encryption setting
- Audic logging

# Resource scaling 
- RPU's hours + storage
- Base RPU's
- Max RPU's
- Expecption: Spectrum, Groups, WM, Partner Integration, Maintnance windows.
- No public endpoints. Must use in VPC.
- Monitoring views: STS_QUERY_HISTORY, LOAD_HISTORY, SERVERLESS_USAGE
- CloudWacth logs, metrics.

# RDS
- Small data
- Hosted relationa database. 
- Not for "big data"
- ACID compliance: Atomaticity, Consistency, Isolation, Durability.

# Aurora
- MySQL and PostgeSQL
- 5x faster MySQL and 3x Postgres
- 1/10 cost
- backup to S3.
- Replication across availabilty zones.
- Automatic scaling with Aurora Serverless.
- VPC isolation. At-rest KML, Intransist SSL.


