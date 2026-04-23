import boto3

# 1. Connect to S3
s3 = boto3.client('s3')

# 2. Specify your bucket name
target_bucket = 'acquantan'

# 3. Ask S3 for the list of objects
response = s3.list_objects_v2(Bucket=target_bucket)

# 4. Check if the bucket actually has files
if 'Contents' in response:
    print(f"Files in {target_bucket}:")
    for obj in response['Contents']:
        print(f" - {obj['Key']}") # 'Key' is the S3 term for filename
else:
    print("The bucket is empty.")