# Charge-Management-API (Python) 
# Objective:-
A set of RESTful APIs to manage charges related to loans for a financial organization. The APIs allows for retrieving, creating, updating, and managing various types of charges associated with loan applications 
and loan accounts. The solution is implemented using Python (AWS Lambda) , and Dynamodb database. 

# AWS Services Used:- 

1) Amazon Lmabda Function:-
AWS Lambda is a serverless compute service offered by Amazon Web Services. It is designed to enable developers to create and run code without having to manage infrastructure. Lambda functions are executed in response to events, allowing developers to build reactive and event-driven applications. They can be written in a variety of languages including Node.js, Python, Ruby, Java, C#, and Go. Lambda functions can be used to perform a wide range of tasks, such as processing data, triggering other AWS services, or even integrating with third-party APIs.

2) Dynamodb:-
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. With DynamoDB, you can create database tables that can store and retrieve any amount of data and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation. You can use the AWS Management Console to monitor resource utilization and performance metrics.

3) API Gateway:-
AWS API Gateway is a fully managed service that makes it easy to create, deploy, and manage RESTful web APIs. It provides a simple and intuitive console for developers, as well as support for integrating APIs with other AWS services. With API Gateway, developers can secure their APIs using RESTful API design principles, and AWS will handle the underlying infrastructure.

4) IAM Role:-
An IAM role in AWS (Amazon Web Services) is a set of permissions that define what actions a user, group, or service can take on AWS resources. IAM roles provide a way to manage access to AWS resources in a secure and efficient manner. You can create and manage IAM roles using the AWS Management Console, the AWS CLI, or the AWS SDKs. An IAM role can be used to grant permissions to any number of resources, including EC2 instances, Elastic Load Balancers, and S3 buckets.

# Endpoints of API:- 
1) /charge:- Used to create , update , delete , retrieve single entry from database.
   Mathods used:-
   a) Create- POST
   b) Update- PATCH
   c) Delete- DELETE
   d) Retrieve- POST
2) /charges:- Used to retrive all the loan charges in database. Method Used- GET 
3) /status:- Used to check that service is operation or not. Method Used- GET

# Functions in Code:- 
1) 


