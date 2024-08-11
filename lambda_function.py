import json
import boto3

dynamodb = boto3.client('dynamodb')
ses = boto3.client('ses')
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Process the event
    item = event['detail']
    
    # Store data in DynamoDB
    dynamodb.put_item(
        TableName='YourDynamoDBTable',
        Item={
            'id': {'S': item['id']},
            'data': {'S': item['data']}
        }
    )
    
    # Send an email with SES
    ses.send_email(
        Source='your_verified_email@example.com',
        Destination={
            'ToAddresses': ['recipient@example.com']
        },
        Message={
            'Subject': {'Data': 'New Event'},
            'Body': {'Text': {'Data': f"New event received: {json.dumps(item)}"}}
        }
    )
    
    # Send a notification with SNS
    sns.publish(
        TopicArn='arn:aws:sns:your_topic_arn',
        Message=f"New event received: {json.dumps(item)}"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully')
    }
