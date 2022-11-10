import boto3

resource_s3 = boto3.client("s3")
# get the list of buckets from S3
get_response = resource_s3.list_buckets()
buckets = get_response["Buckets"]

for bucket in buckets:
    print("S3 bucket name : ",bucket["Name"])