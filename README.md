# COVID-19 Serverless Monitor and Notification App on Amazon Web Services (AWS)
## AWS Serverless cloud-based scraper that monitors COVID19 cases and send notifications on case numbers.

This serverless app is written in Python and uses the Amazon Web Services (AWS) platform: EventBridge, Lambda, S3, and SMS, to monitor the number of COVID-19 cases in a given state in the US and send notifications via text messages if the number of cases changes.

<img src="https://user-images.githubusercontent.com/25143822/171071316-c2889ff6-ea21-409c-8a71-67bd258a5726.png" width="50%" height="50%">

1. A rule in **Amazon EventBridge** is scheduled to run an event every hour. The event is routed to an **AWS Lambda** function as the target associated with the rule.
2. The **AWS Lambda** function calls a **Lambda Layer** that reaches to the website worldometer.com and bring up a webpage with COVID-19 cases for a given state in the US passed as a parameter.
3. The **Lambda Layer** function extracts the COVID-19 data, transforms the data to JSON and passes it back to the **AWS Lambda** calling function.
4. The **Lambda** function saves the JSON file to an **S3 Bucket**.
5. The **Lambda** function reads the prior number of COVID-19 cases from an **S3 Bucket**.
6. The **Lambda** function compares current number of COVID-19 cases to the prior stored number, if there is a difference, then an **AWS Simple Notification Service** (SNS) is called.
7. The **AWS Simple Notification** Service sends a message notification to a predefined phone number using mobile text notification (SMS)

## Reference Architecture
<img src="https://user-images.githubusercontent.com/25143822/171071771-7e10c256-3df4-4a73-89e6-0c7c4835e0b9.png">

## References
Working with AWS SNS and boto3 -
https://towardsdatascience.com/working-with-amazon-sns-with-boto3-7acb1347622d

Python SDK in AWS CLoud9 IDE - https://www.cloud-plusplus.com/post/python-sdk-in-aws-cloud9-ide

 sudo python3 -m pip install requests  
 sudo python3 -m pip install bs4 

