# QuickSight
- Cloud-powered business analytics service
- Build visualizations, Ad-hoc analysis, Business insights.
- Redshift, Athena, Aurora/RDS, S3, on-premise, EC2-hosted databases.
- Allows limited ETL.
- Dataset are imported into SPICE
- Super-fast, Parallel, In-memory, Calculation Engine.
- Columnar stora, in-memory, machine code genaration
- Each user gets 10GB of SPICE

- Use cases: Ad-hoc exploration / visualization of data. Dashboards and KPI's.
- Visualiza data form : S3, On-premise,  AWS DB, SaaS aplication, Salesforce, JDBC/ODBC data source.

- Highly formatted canned reports.
- ETL. Glue instead.

# Security
- VPC Connectivity
- Row-levle security. Single level
- CLS - column privice
- Private VPC acesses
- Resource access
- Data Access - IAM polices to restric user.
- Quicksight + Redshift.
    - Quicksight - access data store in the same region.
    - Solution: create a new security group with an inbound rule authorizing access from the IP range of QuickSight servers in that region.
    - User defined via IAM, Email signup 
    - Activate Directory with QuickSight Enterprise. Cannot use custer provided keys.
    - Enterprise edition only. Security access using IAM.

- Visualizations
- ML Insights: Anomaly detection and forcasting: Randowm Cut Forest. Detects seasonality and trends. Exclude outliers.
- Autonarratives - story of your data
- Suggested Insights.

- Quicksight Q
- Answers using NLP.
-  