import json
import boto3
import os

dynamodb=boto3.client('dynamodb')

def handler(event, context):
    connectionId=event['requestContext']['connectionId']

    dynamodb.delete_item(
        TableName=os.environ.get('TABLE_NAME'),
        Key={'socketId':{'S':connectionId}}
    )
    return {}
