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