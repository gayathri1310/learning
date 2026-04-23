import boto3

s3 = boto3.client('s3')

s3.upload_file('sample.txt', 'acquantan', 'uploaded_sample.txt')
print('File uploaded successfully!')

