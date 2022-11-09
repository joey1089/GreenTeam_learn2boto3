import boto3
from boto3 import Session #not needed if we have boto3 imported alread 

boto_sess = Session(profile_name='useBoto3') # selects useBoto3 aws cli profile 
s3 = boto3.client("s3")
list_s3 = s3.list_objects(Bucket="s3")["Contents"]
print(len(list_s3))
print(s3)
try:
    del s3

except:
    print("failed")

print("Looks like S3 is Deleted !")