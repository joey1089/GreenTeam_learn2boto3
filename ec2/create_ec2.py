# Here we create EC2 Instances and list the created EC2 Instances
import boto3

getObj_ec2 = boto3.client('ec2')

def create_ec2(ec2Obj,Min,Max,imageid,instancetype):
    
    get_response = ec2Obj.run_instances(ImageId=imageid,
            InstanceType=instancetype,
            MinCount=Min,
            MaxCount=Max,
            KeyName= 'GreenTeam_Week14_Project',
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags':
                    [
                    {'Key': 'Name','Value': 'Dev Server'},
                    {'Key': 'Environment','Value': 'Dev'}
                    ]
                },
                        ],
                        )
    
    return get_response['Instances']

get_min = int(input("whats the minimum no of EC2 instance : "))
get_max = int(input("Whats the maximum no of EC2 Instance : "))
get_imageid = str(input("Input your imageid : ")) #(amazon linux ami-id) ami-09d3b3274b6c5d4aa for t2.micro 
get_instancetype = str(input("Input your Instance Type : "))
get_created_ec2 = create_ec2(getObj_ec2,get_min,get_max,get_imageid,get_instancetype)
print("List of Created Instances : ")
for instance in get_created_ec2:
    print(f"Instance ID : {instance['InstanceId']} , Type : {instance['InstanceType']}")