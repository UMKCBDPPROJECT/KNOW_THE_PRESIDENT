import boto3

s3 = boto3.client('s3')

s3.upload_file('data1.json', 'sentiment1', 'data.json')

