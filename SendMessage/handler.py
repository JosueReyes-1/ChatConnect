import json
import urllib3
import boto3
import os

client=boto3.client('apigatewaymanagementapi',endpoint_url='https://f3zuv1ax80.execute-api.us-east-1.amazonaws.com/production')
dynamodb=boto3.client('dynamodb')

def handler(event, context):
    print(event)

    paginator=dynamodb.get_paginator('scan')
    connectionIds=[]
    tableName=os.environ.get('TABLE_NAME')

    for page in paginator.paginate(TableName=tableName):
        connectionIds.extend(page['Items'])
    
    body=json.loads(event['body'])
    responseMessage=body['message']

    for connectionId in connectionIds:
        response=client.post_to_connection(ConnectionId=connectionId['socketId']['S'],Data=json.dumps(responseMessage).encode('utf-8'))
    return {"statusCode":200}

    