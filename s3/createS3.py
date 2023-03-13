# This code creates S3 Buckets
# Use aws configure in awscli to pass the access key
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist


def create_S3_bucket():
    # gets the list of buckets from S3
    # resource_s3_list = boto3.client("s3")
    # get_response = resource_s3_list.list_buckets()
    # buckets = get_response["Buckets"]

    # for bucket in buckets:
    #     print("S3 bucket name : ",bucket["Name"])
    S3_bucket_list = ','.join(map(str,get_bucketlist()))
    print("Current S3 bucket list : ", S3_bucket_list)


    # Create a new bucket
    resource_s3 = boto3.resource("s3")
    get_userinput = str(input("Enter the unique bucket name : "))
    get_bucketname = resource_s3.Bucket(get_userinput)
    # Creates a bucket with ACL as public read
    # response = get_bucketname.create_bucket() doesn't accept arugments without Bucket passed

    response = get_bucketname.create(  
        ACL = 'private',
        # CreateBucketConfiguration={
        #     'LocationConstraint': 'us-east-1' #check why only us-east-2 is accepted
        # },
    )
    print("s3 response :",response)
    return response

create_S3_bucket()