# Machine Learning on AWS
![]()

# What is machine learning
Machine learning systems predict some unknown property of and item, given its other properties.

# Types of machine learning
- Supervised.
- System uses historical data to predict a label.
    - In our training dataset contains labels known to be correct, together with other atributes of the data (features).
    - This training data is used to build a model that can make predictions of unknown labels.
    - Classification, Regression

- Unsupervised
Machine learning systems can also be used for grouping observations. This type of models is called Clustering. Some examples of algorithms for these are: hierarchical modeling, Kmeans, DBSCAN, Bayesian Modeling

There are also other types of machine learing models. Ones that are getting more notice this days are Deep Learning (Computing Vision, NLP Models), GANS, Reiforment learning, Active Learning, Transfer learning.

## Steps for Machine Learning

- Feature Engineering: Construct new features, normalize our data, remove missing data points.
- Training: Where we separate our data into training and testing. And construct a training model and validate with our testing data. With this we try to get our best model performance (accuracy, recall, precision, ROC, ...) and reduce bias and variance.
- Deploying: Deploying our solution and predict new values.

# On AWS

Here I will show an example of architeture that you can build for a simple ML model for production. There are a lot of differente ways you can architect a ML solution. This is only one of them.

![]()

## S3
- It's a place where you can storage your files.
- It helps to storage large amount of data. These data can later be used to train and predict.

## ECR
- ECR is aws container repository. Where you can save your docker image model with your code and dependencies.
- Kedro - is a platform that you can build your data science pipelines.

## Lambda
It is a AWS Service used integrating services and processing data.
- In this example we integrate S3 with Sagemaker.

## Amazon Sagemaker
This is a scalable, fully-managed machine learning service in AWS.
Here you can create your own machine learing.
- Build models using jupyter notebook. It supports GPU, Anaconda package, python, keras.
- Train module - Training and tuning
- Deploy - endpoint your application
- Capture and Visualize Model Metrics.

In this part we will use Sagemaker processing power to run our application.

# Other components
Some other components that you can include to get most of your model.

## CloudWatch
- Metric and evaluation. Then trigger lambda for retraing.

## Data Validation with Great Expectations.
- For your data validation. Than you can compare different versions of your data in order to see if you have a data drift.

## Model Versioning with MLFLOW.
- MLFLOW can help you with feature metrics, model versioning and other features. Recently it has realsed a new feature for pipelines.