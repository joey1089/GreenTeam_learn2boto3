import boto3

resource_s3 = boto3.resource("s3")
# Creates a bucket with ACL as public read
response = resource_s3.create_bucket(
    Bucket='sampleboto3buckettest01',
    ACL = 'public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)

print(response)


