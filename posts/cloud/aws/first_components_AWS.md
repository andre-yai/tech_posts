
![Cloud AWS](https://cloudcomputinggate.com/wp-content/uploads/2022/03/AWS-Cloud-Foundation.jpg)
# Serviços AWS que todos deveriam conhecer.

Atualmente muitas empresas estão cada vez mais migrando as aplicações dos seus próprios servidores para os ambientes cloud.As aplicações em cloud trazem algumas vantagens como escalabilidade, custo, velocidade,  performance, segurança e disaster recovery.

As grandes plataformas que se destacam nesta corrida são a Amazon Web Services (AWS), Azure Microsoft e Google Cloud Platform (GCP).

# Serviços
A seguir irei descrever os serviços que mais se destacam nestes cenários na AWS:

## EC2
Este serviço oferece imagens de maquina da Amazon (AMI). É um ambiente gerenciado e controlado pelo próprio usuário. Apresenta a funcionalidade de auto-scaling e suporta imagens de diversos sistemas operacionais (Linux, Windows, MacOs, entre outros). 
Custo: O nível gratuito da AWS inclui 750 horas de instâncias Linux e Windows t2.micro (t3.micro para as regiões nas quais t2.micro não está disponível) todo mês durante um ano. Para permanecer no nível gratuito, use somente microinstâncias do EC2 (texto da AWS)
[Para mais informações sobre EC2.](https://aws.amazon.com/pt/ec2/features/) 


## Lambda
Este é um serviço computacional auto-gerenciável que executa código em resposta a eventos e é capaz de integrar vários serviços AWS.
Custo: O nível gratuito do AWS Lambda inclui um milhão de solicitações gratuitas por mês e 400.000 GB/segundo de tempo de computação por mês, utilizáveis para funções habilitadas por processadores x86 e Graviton2, em conjunto. - Texto da própria AWS.
[Para mais informações sobre Lambda.](https://aws.amazon.com/pt/lambda/features/)


## S3 - Simple Storage Service.
Este é responsável pelo sistema de armazenamento de dados. Nele podemos gravar uma grande quantia de informação. Além de oferecer escalabilidade, disponibilidade de dados, segurança e alta performace. 
Custo: Pague somente pelo que usar. Não há cobrança mínima. Existem seis componentes de custo do Amazon S3 a serem considerados ao armazenar e gerenciar seus dados: preços de armazenamento, preços de solicitação e recuperação de dados, preços de transferência de dados e aceleração de transferência, preços de análises e gerenciamento de dados, preço de replicação, bem como o preço para processar seus dados com o S3 Object Lambda. - Texto da AWS.
[Para mais informações sobre S3:](https://aws.amazon.com/pt/s3/features/)

## RDS 
Este é uma coleção de serviços gerenciados que facilita a configuração, operação e escalbilidade de banco relacional na AWS. Podemos escolher armazenar as informações com PostgreSQL, MariaDB, Oracle, Aurora, MySQl, entre outros.

## Outros Serviços
Temos vários outros serviços na AWS para diferentes funcionalidades, por exemplo: 

Segurança e Permissão: IAM
Web - Routing (Route53), Distribuição de Sites (CloudFront), Disponibilidade de Aplicações (Beanstalk), Agendamento das oprações (EventBridge), API Gateway, entre outros

Monitoramento - logs das aplicações (CloudWatch), performance da API (CloudTrail) 

Ingestão de dados: tempo real e near real time (Kinesis, SQS, Kafka Connect), batch (DMS, Cloud Connect).

Processamento de dados: Glue, EMR, Step Functions

Armazenamento de dados: EBS, Aurora, DynamoDB, Redshift, Athena.

Visualização de Dados: QuickSight

Machine Learning : Sagemaker