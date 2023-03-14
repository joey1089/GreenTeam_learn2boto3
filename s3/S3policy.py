import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist
import logging

def check_bucket_status(bucket_list):
    """ This method checks if bucket has public access or private access. """
    s3_client = boto3.client("s3")
    try:
        #TODO:2 - need to be fixed and tested
        for bucket_name in bucket_list:
            response = s3_client.get_bucket_policy_status(Bucket=bucket_name)
        return response["PolicyStatus"]
    except ClientError as e:
        # if you do not have any policy attached to bucket it will throw error
        # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
        # The bucket policy does not exist
        print("No policy attached to this bucket")

def set_bucket_policy():
    """ This method adds public policy to a bucket. """
    # policy for making all objects in bucket public by default
    public_policy = """{
      "Id": "Policy1577423306792",
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "Stmt1577423305093",
          "Action": "s3:*",
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::testbucket-frompython-2/*",
          "Principal": {
            "AWS": [
              "*"
            ]
          }
        }
      ]
    }"""
    s3_client = boto3.client("s3")
    bucket_list = get_bucketlist()
    try:
        #TODO:1 - need to be fixed
        response = s3_client.put_bucket_policy(
            Bucket=bucket_list, Policy=public_policy
        )
        print(response)
        # checking bucket status. This should show us s3 bucket is public now
        check_bucket_status()
    except ClientError as e:
        # if you do not have any policy attached to bucket it will throw error
        # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
        # The bucket policy does not exist
        logging.error(e)
        # print(e)



S3_bucket_list = get_bucketlist()

# for bucket in buckets:
#     print("S3 bucket name : ",bucket["Name"])
if S3_bucket_list != False:
    print(check_bucket_status(S3_bucket_list))
else:
    print("\n No S3 Buckets exist in the account! \n")