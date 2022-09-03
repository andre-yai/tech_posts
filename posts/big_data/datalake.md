# How to build a DataLake

## Definition and why now?
With the expansion of big data many industries has been looking for ways to storage their data. One way to do so is by using datalake. 

Datalake is a system or repository of data stored in raw format or replica of business data. It can store data of all types, structured or unstructured.

A data lake provides diverse analytics capabilities, including batch processing, stream computing, interactive analytics and machine learning, along with job scheduling and managed capabilities.

For a data science teams having a data lakes helps by providing a data with no silos and also with raw data great for exploring different kind of databases.

Despites their pros, datalakes lack in certain aspects like data quality and governance and poor optimizations.

Reliablity issue: Without the proper tools in place, data lakes can suffer from data reliability issues that make it difficult for data scientists and analysts to reason about the data. These issues can stem from difficulty combining batch and streaming data, data corruption and other factors. 

Slow performance: As the size of the data in a data lake increases, the performance of traditional query engines has traditionally gotten slower. Some of the bottlenecks include metadata management, improper data partitioning and others.

Lack of security features: Data lakes are hard to properly secure and govern due to the lack of visibility and ability to delete or update data. These limitations make it very difficult to meet the requirements of regulatory bodies.

Data Warehouse is a great way those issues. It provides a strutured schema before ingesting your data. It also provides a better data quality with a single source of true.

## How to build one using cloud.
![Data Lake Image](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2021/07/22/Figure-2.-High-level-design-for-an-AWS-lake-house-implementation.png)

# Ingest 
- Database (OLTP): Data Connect or RDS or EBS.
- Streaming RealTime: Kinesis Data Stream or Kafka
- Streaming NearRealTime: Kinesis Firehouse

# Storage
- Central Storage in S3

# Database with S3
- Athena is a Interactive data Query Service with data located in S3. 

# Processing
- Glue: Processing data in Spark using Python and Scala.
- Lambda: 

# Data Warehouse
- Redshift:

# Machine Learning
- Sagemaker:

## References:
AWS DataLake: https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/
https://databricks.com/discover/data-lakes/introduction

https://aws.amazon.com/blogs/architecture/benefits-of-modernizing-on-premise-analytics-with-an-aws-lake-house/