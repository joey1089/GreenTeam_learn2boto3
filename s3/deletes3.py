import boto3


# resource_s3_list = boto3.client("s3")
# get_response = resource_s3_list.list_buckets()
# buckets = get_response["Buckets"]
# print("Before Deleting buckets count : ",len(buckets))
# for bucket in buckets:
#     print("S3 bucket name : ",bucket["Name"])

# client = boto3.client('s3')
# response = client.delete_bucket(
#     Bucket='checkifitsworks',
# )

# print(response)
# # buckets = get_response["Buckets"] # needs new logic to recount 
# # print('\n After Deletion count :',len(buckets))

def delete_all_objects_from_s3_folder():
    """
    This function deletes all files in a folder from S3 bucket
    :return: None
    """
    bucket_name = "s3bucket4me2test01"

    s3_client = boto3.client("s3")

    # First we list all files in folder
    # response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="images/")
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    files_in_folder = response["Contents"]
    files_to_delete = []
    # We will create Key array to pass to delete_objects function
    for f in files_in_folder:
        files_to_delete.append({"Key": f["Key"]})

    # This will delete all files in a folder
    response = s3_client.delete_objects(
        Bucket=bucket_name, Delete={"Objects": files_to_delete}
    )

    return response

print(delete_all_objects_from_s3_folder())

# ----- new method ---- 
import boto3
import botocore
from botocore.exceptions import ClientError

def listS3():
   client = boto3.client('s3')
   response = client.list_buckets()
   filelist = []
   for bucket in response['Buckets']:
     filelist = bucket['Name']
     print(bucket['Name'])
   return filelist
   
    
def deleteS3(s3,AWS_BUCKET_NAME):  
    resource_s3_list = boto3.client("s3")
    get_response = resource_s3_list.list_buckets()
    buckets = get_response["Buckets"]
    print("Before Deleting buckets count : ",len(buckets))
    print("Before deleting the bucket we need to check if its empty. Cheking ...")
    objects = resource_s3_list.list_objects_v2(Bucket=AWS_BUCKET_NAME)
    fileCount = objects['KeyCount']

    for bucket in buckets:
        print("S3 bucket name : ",bucket["Name"])
    
    # client = boto3.client('s3')
    if fileCount == 0:
         response = resource_s3_list.delete_bucket(Bucket=AWS_BUCKET_NAME)
         print("{} has been deleted successfully !!!".format(AWS_BUCKET_NAME))
    else:
         print("{} is not empty, {} objects present".format(AWS_BUCKET_NAME,fileCount))
         print("Deleting Objects inside S3 bucket")
         resource_s3_list.delete_object(Bucket='AWS_BUCKET_NAME', Key='folder/file_client.txt') # Make Sure Access is given to delete
         
         

    
    
# A Good practice before deleting files is to download if needed for references
BUCKET_NAME = 'mynews3bucket2test01' # replace with your bucket name
KEY = 'test03.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'test03.txt') #this downloads to the current location execution file
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
print("List all the S3 Buckets : \n",listS3())
print("Deleting S3 buckets now ... ", deleteS3(s3,BUCKET_NAME))
