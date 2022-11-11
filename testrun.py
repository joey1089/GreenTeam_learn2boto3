import boto3
# bash this cmd gives iam users list - "aws iam list-users"
# from boto3 import Session #not needed if we have boto3 imported already 
# boto_sess = Session(profile_name='useBoto3') # selects useBoto3 aws cli profile 
# aws_resource_s3 = boto3.client("s3") # created a s3 object
#response = s3.describe_instance() # AttributeError: 'S3' object has no attribute 'describe_instance' 
#print(response)
# list_s3_obj = s3.list_objects(Bucket="s3")["Contents"] # work after cli profile configuration
# print(len(list_s3_obj))

# List out the bucket name in S3
# response = aws_resource_s3.list_buckets()
# buckets = response["Buckets"]

# for bucket in buckets:
#     print("S3 bucket name : ",bucket["Name"])


# print("Created S3 object : ",s3)
# try:
#     del s3

# except:
#     print("failed")

# print("Looks like S3 is Deleted !")

#
client = boto3.client('translate')

def translate_text(): # translate given in target language 
    #https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 
    for text in response:
        print("Translated Text : ",text[4])

translate_text() # This line will call our function. Without it, python will not do anything.
