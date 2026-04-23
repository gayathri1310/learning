import boto3
from dotenv import load_dotenv
import os

load_dotenv() 

Access_key_Id = os.getenv('Access_key_Id')
Secret_Access_Key = os.getenv('Secret_Access_Key')

region = 'ap-south-2'
s3 = boto3.client('s3', aws_access_key_id=Access_key_Id, aws_secret_access_key=Secret_Access_Key, region_name=region)

s3.create_bucket(
    Bucket='acquantan3',
    CreateBucketConfiguration={'LocationConstraint': region}
)

print('Bucket created successfully!')
