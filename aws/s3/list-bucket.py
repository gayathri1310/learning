import boto3
from dotenv import load_dotenv
import os

load_dotenv() 

Access_key_Id = os.getenv('Access_key_Id')
Secret_Access_Key = os.getenv('Secret_Access_Key')

s3 = boto3.resource('s3', aws_access_key_id=Access_key_Id, aws_secret_access_key=Secret_Access_Key) 

for bucket in s3.buckets.all():
    print(bucket.name)