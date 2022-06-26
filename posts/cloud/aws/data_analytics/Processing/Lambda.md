
# Lambda
Serverless data processing
- Serverless
- Continuous scalling
- Glue between different services.

- FROM: Data Stream
- TO: DynamoDB, SNS

Servers: not cheap, management.
- Main uses of Lambda.
- ETL
- Real-time processing
- Real-time stream processing
- Cron replacement
- Process AWS events.

Lambda triggers:
- S3, SES, Firehouse, Data Streams. Dynamodb, SQS, SNS, Config, IOT Button, Lex, CloudWatch, CloudFormation, API Gateway, CloudFront, Cognito, CodeCommit.

FROM: S3
To: ElasticSearch Service, Data Pipeline
When: It is received.

S3 => Lambda => Redshift.
- DynamoDB - save states.

Lambda => Kinesis.
- Batch: size up to 10,000 records. To large can cause timeouts.
- Also payload limit 6 MB.
- Lambda Will retry until it succeds or data expires.
    - This can stall the shard if you dont handle errors properly.
    - use more  shards.
- Lambda processes shard synchornously.

## Cost 
- Pay for what you use.
- Generous free tier.
- Very cheap.

- High availability.
- Unlimited Scalability. 1.000 records.
- High performance.

- Anti-patterns
- Long running applications: Use EC2 instead. Or chain functions
- Dynamic websites: client side AJAX
- Stateful applications: DynamoDB or S3 to keep track of state.