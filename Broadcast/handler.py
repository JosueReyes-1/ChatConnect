import json
import urllib3
import boto3

client=boto3.client('apigatewaymanagementapi',endpoint_url='https://f3zuv1ax80.execute-api.us-east-1.amazonaws.com/production')

def handler(event, context):
    print(event)

    connectionId=event['connectionId']

    # body=json.loads(event['body'])
    responseMessage=event['message']

    response=client.post_to_connection(ConnectionId=connectionId,Data=json.dumps(responseMessage).encode('utf-8'))

    return {"statusCode":200}

    