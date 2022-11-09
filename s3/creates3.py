import boto3

resource_s3 = boto3.resource("s3")
# Creates a bucket with ACL as public read
response = resource_s3.create_bucket(
    Bucket='boto3createdbucket',
    ACL = 'public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },
)

print(response)


