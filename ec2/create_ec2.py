# Here we create EC2 Instances and list the created EC2 Instances
import boto3

def create_ec2(Min,Max,imageid,instancetype):
    create_ec2 = boto3.client('ec2')
    get_response = create_ec2.run_instances(ImageId=imageid,
            InstanceType=instancetype,
            MinCount=Min,
            MaxCount=Max,
            KeyName= 'GreenTeam_Week14_Project',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name','Value': 'Dev Server'},
                    {'Key': 'Environment','Value': 'Dev'}]
                },
                        ],
                        )
    return get_response['Instances']

get_min = int(input("whats the minimum no of EC2 instance : "))
get_max = int(input("Whats the maximum no of EC2 Instance : "))
get_imageid = str(input("Input your imageid : ")) #(amazon linux ami-id) ami-09d3b3274b6c5d4aa for t2.micro 
get_instancetype = str(input("Input your Instance Type : "))
get_created_ec2 = create_ec2(get_min,get_max,get_imageid,get_instancetype)
print("List of Created Instances : ")
for instance in get_created_ec2:
    print(f"Instance ID : {instance['InstanceId']} , Type : {instance['InstanceType']}")



# 'Instances':[{'AmiLaunchIndex': 0, 'ImageId': 'ami-09d3b3274b6c5d4aa', 'InstanceId': 'i-0773173a1ab6a6867', 'InstanceType': 't2.micro', 
# 'KeyName': 'GreenTeam_Week14_Code', 'LaunchTime': datetime.datetime(20...o=tzutc()), 'Monitoring': {...}, 'Placement': {...}, 'PrivateDnsName': 'ip-172-31-93-35.ec2.internal', ...}]
# Full Response = {'Groups': [], 'Instances': [{...}], 'OwnerId': '282495905450', 'ReservationId': 'r-043b46aa51822cb3c', 
# 'ResponseMetadata': {'RequestId': '8d1beae1-217f-4945-9...b0ed14420c', 'HTTPStatusCode': 200, 'HTTPHeaders': {...}, 'RetryAttempts': 0}}