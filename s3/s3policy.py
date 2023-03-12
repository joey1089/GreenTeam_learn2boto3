import boto3
import ex

def check_bucket_status():
    """
    This function checks if bucket has public access ot private access.
    :return: None
    """
    s3_client = boto3.client("s3")
    try:
        response = s3_client.get_bucket_policy_status(Bucket="testbucket-frompython-2")
        print(response["PolicyStatus"])
    except ClientError as e:
        # if you do not have any policy attached to bucket it will throw error
        # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
        # The bucket policy does not exist
        print("No policy attached to this bucket")

def set_bucket_policy():
    """
    This function adds policy to bucket.
    :return: None
    """
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

    try:
        response = s3_client.put_bucket_policy(
            Bucket="testbucket-frompython-2", Policy=public_policy
        )
        print(response)
        # checking bucket status. This should show us s3 bucket is public now
        check_bucket_status()
    except ClientError as e:
        # if you do not have any policy attached to bucket it will throw error
        # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
        # The bucket policy does not exist
        print(e)