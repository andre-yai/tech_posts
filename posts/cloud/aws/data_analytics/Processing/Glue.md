# Glue

Serverless discovery and definition of table definitions and schema
S3 "data lakes""
- RDS
- Redshift
- Most SQL databases
- metadata repository
- extract structure from unstructured data
- Discover schema
- Custom ETL jobs.
- Trigger-driven, on a schedule, or on demand
- Fully managed.


Glue Crawler./ Data Catalog

- scans data in S3.
- run periodically
- Populates the Glue Data Catalog
    - Stores only table definition
    - Stays on S3.
- Treat you unstructed data like structured
    - Redshift 
    - Athena
    - EMR
    - Quicksight
- Think how do you organize your data.
- Top level partition matters
- Time ranges yyyy/mm/dd/devices
- Device: device/yyyy/mm/dd/

## Apache Hive
= Hive matastore to GLUE.
- SQL like queries EMR

## GLUE ETL
- generate code
- scala or python
- server-side or SSL
- can be event-driven
- DPU's to increase underlying Spark Jobs.
- Errors reported to CloudWatch.
- Transform, Clean Data, Enrich Data
- Generate ETL code
- Can provide your own Spark or Pyspark scripts.
- S3, JDBC or in Glue Data Catalog.
- Serverless Spark platform

Dynamic Fram.
- More ETL available
- DynamicRecodes are self-describing 
- DropFields, DropNullFilds
- Filter
- Join
- Map - add fields, perform external 
MachineLearning Transformations:
- FindMatches ML : identify duplicate or matching records in your dataset, even do not have a unique identifier
- Formart convert: CSV, JSON, Avro, Parquet, ORC, XML
- Spark transformation
- ResolveChoice: deal with ambiguities.
    - two fileds with same name, make_cols
    - cast, make_struct, projects.

- Modifying Data Catalog.
- Glue ETl. Update schema and partitions if necessariy.
- New partitions: Re-run crawler or use enableUpdateCatalog and partitionsKeys options.
- Update table schema: Re-run crawler or use enableUpdateCatalog, updateBehavior from script.
- Creating new tables: enableUpdateCatalog, UpdateBehavior with setCatalogInfo.

Restrition
- S3 only.
- Json, csv, avro, parquet only
- Parquet requires special code
- Nested schemas are not supported

- Develop ETL scripts using a notebook
- Then create an ETL job that runs your script.
- Endpoint is in a VPC controlled by security groups, connect via: 
    - Zepplin on your local machine
    - Zepplin notebook server on EC2
    - SageMaker notebook
    - Terminal window
    - PyCharm professional edition
    - Use Elastic IP's to access a private endpoint address.
    - Cron time based schedule
    - Job bookmarks.
    - persists state form job run
    - S3 soruces in varity of formats 
    - new rows not updated rows

    - CloudWatich Events.
    - Fireoff a Lambda function or SNS notification when ERL succeeds or fails.
    - Invole EC2 run, send event to Kinesis, activate a Step Function.

    - Cost model.
    - By minute fro crawler and ETL job.
    - Development endponts charged by minute.
    - Avoid multiple: Multiple ETL engines. 
        - Based on SPark
        - Other engines (Hive, Pig, etc) Data Pipeline EMR would be a better fit.

    - Glue ETL : streaming. Supports serverless streaming ETL. 
    - Consumes from Kinesis or Kafka.
    - Clean and transform in-flight
    - Store results into S3 or other data stores.
    - Runs on Apache Spark Structured Streaming

## Glue Studio
- Visual interface for ETL workflows.
- Visual job editor.
    - Cretate DAG's for complex workflows.
    - Soruces include S3, Kinesis, Kafka, JDBC.
    - Transform simple data.
    - Target to S3 or Glue Data Catalog.
    - Support Partitioning
- Visual job dashboard.

## Data Brew
- Visual data preparation Tool.
- More simple than DataBrew. 
- Transform data in some way.
- Missing, Filtering
- Format on s3. Data quality.
- Custom SQl.

## Glue Elastic Views
-  Materialized views from Aurora, RDS , DynamoDB.
- SQL interfacem copying or combining data.
- Monitors continuously updates.

# AWS Lake Formation
- Make easy to set up data lake 
- Loading data & monitoing data flows.
- Top of Glue.
- Migrating data to Data Lake.
- IAM permissions.
- Not support manifest.
- Blueprint or workflow.
- Supports "Governed Tables"ACID transations.
- Automatic Compaction.
- Control Acces to Row and Cell Level.
- Data Permission: Column and Rows. Managed in UI.