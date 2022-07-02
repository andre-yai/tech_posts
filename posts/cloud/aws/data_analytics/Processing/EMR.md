# EMR
- Elastic MapReduce
- Managed Hadoop framework on EC2 instance
- Spark, Hadoop.
- Master node: Manages the cluster. Trach status of tasks. Single EC2 instance.
- Core node:  Hosts HDFS data and runs tasks. Can be scaled up & down, but with some risk.Multi-node clusters have at least one
- Task node: Run tasks, does not host data. Optional. No risk of data loss when removing. Good use of spot instances.
- Transient clusters terminate once all steps are complete.
    - save money
- Long-running clusters must be manually terminated.
- Basically a data warehouse with periodic processing on larde datasets
- Can spin up task nodes.

## EMR Usage
- Frameworks and applications are specified at cluster launch.
- Connect directly to master to run jobs directly
- Or submit ordered steps via the console.
    - Process data in S3 or HDFS
    - Output data to S3 or somewhere
    - Once defined, steps can be invoked via the console.

## EMR AWS Integration
- EC2 to comprise data in the cluster
- VPC to configure the virtual network in lunch your instances
- S3 to store input and output data
- CloudWatch to monitor cluster
- IAM to configure permissions
- Cloud Trail to audit requests made to the service
- Data Pipeline to schedule and start your clusters.
### Storage
- HDFS
    - Multiples copies stored accross cluster instances for redundancy.
    - Files stored as blocks
    - Ephemeral 
    - Caching intermediate results 
- EMRFS: access S3 as if were HDFS
    - Allows persistent storage after cluster termination
    - EMRFS Consistent View - Optional for S3 consistancey
    -  DynamoDB to track consistancy
    - 20221L S3 is now consistent Persistency
- Local File System
    - Suitable only for temporary data
- EBS for HDFS
    - Use of EMR on EBS-only types (M4, C4)
    - Deleted when cluster is terminated
    - EBS volumes can only be attached when launching a cluster
    - If you manually detach an EBS volume, EMR treats that as a failure and replaces it.

# Promises
- EMR charges by the hour. Plus EC2 charges
- Provisions new nodes if a core fails
- Can add and remove tasks nodes on the fly
    - Increase processing capacity, but not HDFS capacity.
- Can resize a running cluster's core nodes
    - Increases both processing and HDFS capacity
- Core nodes can also be added or removed
    - But removing risks data loss

EMR Managed Scaling
- EMR Automatic Scaling
    - The old way of doing it
    - Custom scaling rules based on CloudWatch metrics
    - Supports instance groups only
- EMR Managed Scaling
    - Instance groups and instance fleets
    - Scale spots, on-demand and instances in a Savings Plan within the same cluster.
    - Available for Spark, Hive, YARN workloads
- Scale Up Strategy,
    - First add core nodes than task nodes, up to max
- Scale Down Strategy.
    - First remove task nodes, than core nodes, no futher than minimum constraints
    - Spots nodes always before on-demand instances.

# Hadoop
- MapReduce : Framework for distributed data processing. Maps data to key/pairs. Redueces intermediate result to final result. Largerly supplanted by Spark these days.
- Yarn : Yet another resource Negotiator: Manage cluster resources for multiple processign frameworks.
- HDFS : Distributed File System. Distributes data accross cluster in a redudant manner.

## EMR Serverless
- How many nodes it needs.
- Submit queries/ scripts via job run requests.
- EMR manages underlying capacity.
- specify default worker sizes & pre-initialized capacity.
- Big deal. No longer estimate how many nodes needed.
- Not realy serverless needs presto and uses EC2,

# Apache Spark
- Spark: In memory caching. Otimize query.
- Support code reuse accross
- Spark Streming 
- Not for OLTP.

- SPARK CORE: memory management, fault recorvery, scheduling, dietribute & monitor jobs, interact with storage Scala, Java, R.
- SPARK Streaming: Real-time streaming analytics, Structured streaming, Twitter, Kafka, Flume
- SPARK SQL. - Up to 100x faster than MapReduce
- MLIB - ML Algorithms.
- GraphX - Graph, Processing ETL, analysis, Interative graph computation.

- Spark Streaming
- Add write data. 
- Integrate with Kinesis or S3.

# Apache Hive
- On top of map Reduce or tez
- Very close to SQL.
- Interactive
- Scalable - works with "big data" on a cluster.
- Most appropriate for data warehouse applications.
- Easy OLAP queries - WAY easier than writing MapReduce in Java.
- Highly optimized
- Highly extensible: user defined functions, thrift server, JDBC/ ODBC driver.

# HIVE
- Hive maintains a "metastore" that imports a structure you define on the unstructured data that is stored on HDFS.
- External Hive Metastore: is stored in MySQL. But can be stored in Glue data Catalog or RDS or Aurora.
- Load to partitions, Write tables in S3, Load scripts.
- Load partitions from S3, write S3 , load scrpits from S3.

# Pig
- Writing mappers and reducers by hand takes a long time,
- Pig Latin
- Query data in S3, Load from S3.

# HBASE
- Non-relation databsase,
- On top of HDFS.
- In memory. Integrade of Hive.
- DynamoDB - separate service. 
- HBase - efficient sparse data, high frequency counters (consistent reads & writes), High write & update through. More integration with Hadoop.
- Can store data in S3 via EMRFS.

# Presto
- Connect many differente "big data" databases and data stores.
- Interactive queries at petabyte scale
- SQL Syntax.
- Athena uses under the hood.
- HDFS, S3, Cassandra, MongoDB, HBase, SQL, Redshift, Teradata.

# Zepplin Notebook.
- Run Spark interactively.
- Can execute SQL queries directly agains SparkSQl.
- Data Sicence tool.
- EMR Notebook. - Similar  Jupyter.
- Backed up to S3. 
- Hosted inside VPC. Accessed only via AWS console.
- Access via AWS Mangagement Console

# HUE
- Hadoop User Experience
- Graphical front-end for applications on your EMR cluster

# Splunk
- Operational tool
- Splunk makes machine data accessible, usable and valuable to everyone.
- Can be used to visualize EMR and S3 data using your EMR Hadoop cluster.

# Flume
- Log data 
- Stream data into your cluster.
- Biult in HDFS and HBase
- Handle log aggregation.

# MXNet
- Building and accelerating neural networks.
- Included on EMR.

# S3DistCP
- Copying data from:
- S3 to Hdfs.
- HDFS to S3.

- Gangliea : monitoring
- Mahout : Machie learing
- Accumulo : NoSQL database
- Sqoop : database connector
- HCatalog: Table and storage management
- Kinesis Connector 
- Tachyon : Accelarator for Spark
- Derby : DB in Java
- Ranger : security

EMR Security
- IAM policies: permisions
- Kerberos : secure use auth
- SSH : Secure connection 
- IAM Roles: Accessions on user, group.
- Block public access: S3.
