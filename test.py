import boto3
client = boto3.client('s3',region_name='us-west-1')

response = client.create_bucket(
    
    Bucket='rohit-demo-bucket-yt-123',
    CreateBucketConfiguration={'LocationConstraint': 'us-west-1'}
)