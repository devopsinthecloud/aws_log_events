import pandas as pd
import boto3

data = pd.read_csv('devops.csv')

user = data.loc[0, 'User name']
access_key_ID = data.loc[0, 'Access key ID']
secret_access_key = data.loc[0, 'Secret access key']

print(user, access_key_ID, secret_access_key)


client = boto3.client(
    'logs',
    aws_access_key_id=access_key_ID,
    aws_secret_access_key=secret_access_key,
    region_name='us-east-2'
)


logGroupName = 'flask-api-insights'
logStreamNames = ['insights']


response = client.filter_log_events(
    logGroupName=logGroupName,
    logStreamNames=logStreamNames,
    startTime=1627398000000,  # 2021-07-27 15:00 PM UTC
    # endTime=123,
    filterPattern='8cgRlIXOn6QnBCbpYrjSsCnRJjEgRuFl',
    # nextToken='string',
    limit=5
    # interleaved=True|False
)

print(response)
