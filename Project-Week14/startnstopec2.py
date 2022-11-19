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

#Code to start the stopped ec2 instances
import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
def starting_instances(ec2):
    starting_list = []
    stopped_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:Environment','Values':['Dev']}])
    for instance in stopped_instances:
        id=instance.id        
        starting_list.append(ec2.instances.filter(InstanceIds=[id]).start())
    return starting_list

get_starting_list = starting_instances(ec2)


#Code to stop running ec2 instances
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

def stopped_environment_instances(ec2):
    stopped_list = []
    running_environment_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Environment','Values':['Dev']}])
    for instance in running_environment_instances:
        id=instance.id        
        stopped_list.append(ec2.instances.filter(InstanceIds=[id]).stop())
    return stopped_list

    
get_stopped_list = stopped_environment_instances(ec2)
print("Get the response : ",get_stopped_list)

    