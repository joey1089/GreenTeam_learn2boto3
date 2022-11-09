import boto3

resource_s3 = boto3.resource("s3")
get_userinput = str(input("Enter the unique bucket name : "))
get_bucketname = resource_s3.Bucket(get_userinput)
# Creates a bucket with ACL as public read
# response = get_bucketname.create_bucket() doesn't accept arugments without Bucket passed
response = get_bucketname.create(  
    ACL = 'private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)
print("s3 response :",response)
# gets the list of buckets from S3
resource_s3_list = boto3.client("s3")
get_response = resource_s3_list.list_buckets()
buckets = get_response["Buckets"]

for bucket in buckets:
    print("S3 bucket name : ",bucket["Name"])


