# Perspective of Big Data steps and jobs

With the increase of computational and storage power, companies has been collecting more data than ever. This leading the need of new tasks and jobs opportunities. In order to extract value from data companies should rely on data pipelines. This pipelines consist in stages like collection, storage, process and analyzing data.

## Collection
This step is responsable for ingesting data from different sources in order to use them for later analyzes. This data come mainly from realtime and batch sources. 
For realtime data we usually use streaming platform like Kafka, AWS Kinesis, GCP Pub/Sub, Azure PubSub. In this platforms we have those who produce data (Producers) and those who consume data (Consumers). Usually an example of it would be like what Netflix and Spotify uses to send their data to millions of users.
For batch proceses would be to ingest data from an existing database. For example to ingest data from a transactional database like PostgreSQL, MySQl to a data lake or data warehouse like AWS S3, AWS Redshift, GCP BigQuery.

## Storage
Once we collect our data it will need a place be storage.  In this service, by knowing their frequence and need we can  we can control data lifecycle. This going from getting more frequent data to archiving or deleting them. 

Some services that help with that would be AWS S3, GCP Cloud Storage and Azure Blob Storage.

## Process
This came in a raw format so it would usually need a cleaning, enrichment, transforming proccess for a later use. In order to help with it companies has been using tiers like raw, process,refined.

Some services that help with that would be AWS Glue, AWS EMR, AWS Lambda,GCP DataFlow, GCP Functions, Azure DataFactory, Azure Functions.

## Governance
Data governance consists on data management, data quality, data steward. This helps to manage policies to access data, data discovery, data accuracy, validation, completeness.

Some services that help with thare are AWS Glue Catalog, AWS LakeFormation, GCP Data Catalog, GCP Data Loss Prevention.


## Analyze
This part is responsable for extracting value from data by performing data analysis, machine learning and data visualization. This consistis in extracting meaning from data by showing how it is organized, grouping and predicting it.

Some services that help with that would be AWS Sagemaker, AWS QuickSight, GCP BigQuery, GCP Vertex AI, GCP Looker, GCP Data Studio, Azure ML, Azure Databricks, Azure Data Studio.


# Job market

There has been an increase job opportunities

# Data Engineers

# Data Architect

# Data Governance

# Business Inteligence

# Data Scientists

# Machine Learning Engineers/ MLOps Engineers

