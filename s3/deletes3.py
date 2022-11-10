import boto3


resource_s3_list = boto3.client("s3")
get_response = resource_s3_list.list_buckets()
buckets = get_response["Buckets"]
print("Before Deleting buckets count : ",len(buckets))
for bucket in buckets:
    print("S3 bucket name : ",bucket["Name"])

client = boto3.client('s3')
response = client.delete_bucket(
    Bucket='checkifitsworks',
)

print(response)
# buckets = get_response["Buckets"] # needs new logic to count again
# print('\n After Deletion count :',len(buckets))