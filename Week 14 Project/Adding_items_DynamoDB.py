import boto3 
import json

# Create a DynamoDB resource object with the specified access credentials
dynamodb = boto3.resource('dynamodb',
    aws_access_key_id='*************',  # Specify the AWS access key ID
    aws_secret_access_key='*************')  # Specify the AWS secret access key

# Specify the table to work with
table = dynamodb.Table('Movies')

# Use batch_writer to efficiently write multiple items in a batch
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'name': 'The Flash',  # Specify the name attribute
            'rating': 'PG-13'  # Specify the rating attribute
        }
    )
    batch.put_item(
        Item={
            'name': 'Spider-man: Across the Spider-Verse',
            'rating': 'PG'
        }
    )
    batch.put_item(
        Item={
            'name': 'Elemental',
            'rating': 'PG'
        }
    )
    batch.put_item(
        Item={
            'name': 'No Hard Feelings',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'Transformers',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'The Little Mermaid',
            'rating': 'PG'
        }
    )
    batch.put_item(
        Item={
            'name': 'Asteroid City',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'The Blackening',
            'rating': 'R'
        }
    )
    batch.put_item(
        Item={
            'name': 'The Boogeyman',
            'rating': 'PG-13'
        }
    )
    batch.put_item(
        Item={
            'name': 'Fast X',
            'rating': 'PG-13'
        }
    )
