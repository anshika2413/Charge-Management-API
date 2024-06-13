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
1) get_charge:- This method is retrieves the all the information related to a loan charge through its "id" . It takes charge_id as an argument and returns an object containing all the information about the particular charge. It sends GET request to the database and retrieves all the information.
2) get_charges:- This method retrieves all the loan charges present in the database. It also sends the GET request and retrieves all the entries from the database.
3) save_charge:- This methods allows to make a new entry in the database. It takes a json object as an argument and create a new entry in the database. It send a POST request 
4) modify_charge:- This method allow to update the value from the database . It takes charge_id, update_key, update_value as an argument and update the value which is passed as "update_key" in the database. It send a PATCH rquest to update values in the table.

# Working:- 
1.API Request:- A client (like a web app) sends a request to the API Gateway (e.g., to create, read, update, or delete a charge).
2.API Gateway:- API Gateway receives the request and sends it to the appropriate AWS Lambda function(i.e api_pro).
3.Lambda Function:- The Lambda function receives the request and reads the data (like charge details or charge ID).
4.Interact with DynamoDB:- The Lambda function talks to DynamoDB to do the necessary action (add, get, update, or delete a charge record).
5.Prepare Response:- The Lambda function creates a response based on what happened with the DynamoDB operation (e.g., a success message or charge details).
6.Send Response to API Gateway:- The Lambda function sends this response back to the API Gateway.
7.Client Receives Response:- API Gateway sends the final response back to the client, completing the process.


![WhatsApp Image 2024-06-13 at 16 49 45_e838cbb5](https://github.com/anshika2413/Charge-Management-API/assets/112202632/6ff85688-0d4d-4e2d-9c7b-02776405ccc0)

