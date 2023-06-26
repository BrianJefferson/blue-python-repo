import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Specify the queue name
queue_name = 'wk15project'

# Create a queue with the specified name and attributes
response = sqs.create_queue(QueueName=queue_name, Attributes={'DelaySeconds': '0'})

# Extract the queue URL from the response
queue_url = response['QueueUrl']
