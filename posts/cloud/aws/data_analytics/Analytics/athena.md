# Athena
- Serverless interactive queries of S3 data
- Interactive query for S3
- Presto under the hood
- Serverless
- Supports many data formats. Csv, Json, orc (columnar), parquet (Columnar), avro.
- Unstrured, semi-structured, or structured.
- Ad-hoc queries of web logs
- Querying staging data before loading to Redshift
- Analyze CloudTrail/ CloudFront/ VPC/ ELB logs in S3.
- Integration with Jupyter, Zepplin, RStudio notebooks.
- Integration with QuickSight
- Integration via ODBC/JDBC with other visualization tools.

# AWS GLUE and Amazon Athena.
- Use AWS Glue Crawler, Catalog to expose data schema.
- Athena see it.

Athena cannot query accorss regions on its own.
- Buit a Gleu Crawler can.
- Glue Catalog in the same region as Athena.
- Workgroups: organize users/teams/apps/workloads into Workgroups.
- Can access ant track costs by Workgroup.
- Each workgroup can have its own: 
- query history, data limits, IAM polices, Encryption settings.
- Pay as you go. $5 per TB scanned.
- Cancelled queries count.
- Columnar formats. ORC,Parquet better performance and cheaper. Also partition data, hour. MSCK REPAIR Table. Small number of large files performs better than large number of small files.
- Glue and S3 have their own charges.
- Security: Access Control list. IAM ACLS, S3 bucket polices. AmazonAthenaFullAccess.
- Encrypt results at rest in S3.: Server side encryption with S3, KMS key.
- Cross account access in S3 bucket is possible,
- TLS encryts intransit Athena and S3.

# Anti-patterns
- Highly formatted reports/vizualizations. QuickSight
- ETL. Use Glue instead.

# ACID transactions
- Apache Iceberg
- Concurrent users can safely make row-level modifications
- Compatible with EMR, Spark,
- Removes newd for custom record locking
- Time travel operations - Recover data 
- Lake Formation can also govern tables on S3. And to ACID on Athena.
- Benefits from periodic compaction to presere perfomance
