# Serverless-AutoMail

## Architecture
![image](https://github.com/user-attachments/assets/479ec83e-6b8e-4628-8d82-79d42a5f300c)


## Features
  * Automated Email Sending: Automatically sends emails based on specific triggers defined by the user.
  * AWS Integration: Leverages AWS services such as SES (Simple Email Service) for email sending, SNS (Simple Notification Service) for notifications, and Lambda for executing the trigger logic.
  * Customizable Triggers: Easily define and manage triggers that initiate the email sending process.
  * Scalable and Reliable: Built on top of AWS infrastructure, ensuring scalability and reliability.

## Prerequisites
  * An AWS account with the following services set up:
     * Amazon SES (Simple Email Service)
     * Amazon SNS (Simple Notification Service)
     * AWS Lambda
  * AWS CLI configured on your local machine.
  * Python 3.x installed on your local machine.

## Setup
 1. API Gateway - Setup a REST API with the POST Method and notedown the endpoint URL.
 2. AWS EventBridge - Create the event rules as to when the emails need to be sent.
 3. AWS DynamoDB - Create a table with the necessary information such as the email ID and names of the client.
 4. AWS Lambda - Modify the attached JSON with your own details and deploy it on AWS Lambda.
 5. AWS SES - Configure SES by verifying the email IDs of the senders and receivers.
 6. AWS SNS - Create a topic and subscribe to it with your mail ID. Integrate SNS into the Lambda JSON.

## Process
 1. The API Gateway triggers an event.
 2. EventBridge routes the event to the Lambda function.
 3. The Lambda function processes the event, updates DynamoDB, and sends emails and notifications via SES and SNS.

