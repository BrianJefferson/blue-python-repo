import boto3

# Create a DynamoDB resource object with the specified access credentials and region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
    aws_access_key_id='***************',  # Specify the AWS access key ID
    aws_secret_access_key='*****************')  # Specify the AWS secret access key

# Specify the table to work with
table = dynamodb.Table('Movies')

# Perform a scan operation on the table
response = table.scan()

# Extract the items from the response
items = response['Items']

# Iterate over the items and print each item
for item in items:
    print(item)
