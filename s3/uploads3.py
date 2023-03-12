import boto3


def upload2S3(res_s3, buckets):
    ''' Upload files to s3 buckets in the list. '''
    # print(s3)
    for bucket in buckets:
        print(bucket["Name"])
    #write try catch block to catch if file not found error
        
    with open('test01.txt', 'rb') as data:

        res_s3.upload_fileobj(
            Fileobj=data, 
            Bucket='s3bucket4me2test02', 
            Key='text01.txt'
        )
    return


resource_s3 = boto3.client("s3")
# get the list of buckets from S3
get_response = resource_s3.list_buckets()
buckets = get_response["Buckets"]

# for bucket in buckets:
#     print("S3 bucket name : ",bucket["Name"])

upload2S3(resource_s3,buckets)