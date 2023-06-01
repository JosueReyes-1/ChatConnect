import json
import boto3
import os
dynamodbClient=boto3.client('dynamodb')

def handler(event, context):
    print(event)
    tableName=os.environ.get('TABLE_NAME')
    connectionId=event['requestContext']['connectionId']
    print(connectionId)
    item={
        "socketId":{"S":f"{connectionId}"}
    }
    print(item)
    response=dynamodbClient.put_item(
        TableName=tableName,
        Item=item
    )
    print(response)
    return {}
