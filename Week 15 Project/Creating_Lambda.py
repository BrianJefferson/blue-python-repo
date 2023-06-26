import json
import boto3
from datetime import datetime

def lambda_handler(event, context):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    sqs = boto3.client('sqs')

    sqs.send_message(QueueUrl="Your_SQS_Queue_URL", MessageBody=current_time)

    return {
        'statusCode': 200,
        'body': json.dumps('Success! At least we did something correct')
    }