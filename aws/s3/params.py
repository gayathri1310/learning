import boto3 
import os 
from dotenv import load_dotenv

load_dotenv()
Access_key_Id = os.getenv('Access_key_Id')
Secret_Access_Key = os.getenv('Secret_Access_Key')

ssm = boto3.client('ssm', aws_access_key_id=Access_key_Id, aws_secret_access_key=Secret_Access_Key, region_name='ap-south-2')

response = ssm.get_parameter(Name='params-learn', WithDecryption=True)

print(response['Parameter']['Value'])  