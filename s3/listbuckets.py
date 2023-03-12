import boto3


def get_bucketlist():

    resource_s3 = boto3.client("s3")
    # get the list of buckets from S3
    get_response = resource_s3.list_buckets()
    buckets = get_response["Buckets"]
    bucket_list = []

    for bucket in buckets:
        # print("S3 bucket name : ",bucket["Name"])
        bucket_list.append(bucket["Name"])
    return bucket_list      
    
# print(get_bucketlist())