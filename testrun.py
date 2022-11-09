import boto3

s3 = boto3.client("s3")
print(s3)
try:
    del s3

except:
    print("failed")

print("Looks like S3 is Deleted !")