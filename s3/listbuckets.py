# This code returns the list of buckets if it exist in the account
# Use aws configure in awscli to pass the access key
import boto3
from botocore.exceptions import ClientError
import os

def clrscrn():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_bucketlist():
    ''' This method returns list of buckets if found.'''

    resource_s3 = boto3.client("s3")
    # get the list of buckets from S3
    get_response = resource_s3.list_buckets()
    buckets = get_response["Buckets"]
    bucket_list = []

    if buckets != []:
        for bucket in buckets:
            # print("S3 bucket name : ",bucket["Name"])
            bucket_list.append(bucket["Name"])
        return bucket_list    
    else:
        return bucket_list 
    
# print(get_bucketlist())