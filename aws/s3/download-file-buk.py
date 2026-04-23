import boto3

s3 = boto3.client('s3')

s3.download_file('acquantan', 'workday-finance-system-api-1.0.0-raml/workday-finance-system-api.raml', 'downloaded_raml.raml')

print('File downloaded successfully!')

