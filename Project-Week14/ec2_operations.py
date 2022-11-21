#The plan of this project is to start and stop ec2 instances as and when needed but also terminate instances whenever the user wants
# Here we create EC2 Instances and list the created EC2 Instances
#<----- Work pending in intergration to call each fn to perform operations whenever needed ------>
#<----- Prior to running this code, 1.install aws cli then set aws configure and install pip, then boto3 ------>
import boto3
import os


def clr_scrn():
    '''This method clears the screen'''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

# Resources Objects are created here
getObj_ec2 = boto3.client('ec2') # Resource object to create the ec2 instances
stop_ec2 = boto3.resource('ec2', region_name='us-east-1') # Resource Object to stop the ec2 instances
start_ec2 = boto3.resource('ec2', region_name='us-east-1') # Resource Object to start the ec2 instances
terminate_ec2 = boto3.client('ec2') # Resources Object to terminate the ec2 instances
list_instances = boto3.resource('ec2', region_name='us-east-1') # Resource Object to list running ec2 instances


def create_ec2(ec2Obj,Min,Max,imageid,instancetype):
    '''Fn to create ec2 instances'''
    
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


#Code to start the stopped ec2 instances
def starting_instances(ec2):
    '''Start the stopped ec2 instances'''
    starting_list = []
    stopped_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:Environment','Values':['Dev']}])
    for instance in stopped_instances:
        id=instance.id        
        starting_list.append(ec2.instances.filter(InstanceIds=[id]).start())
    return starting_list

#Code to stop running ec2 instances
def stopped_environment_instances(ec2):
    '''Stop the ec2 instances'''
    stopped_list = []
    running_environment_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Environment','Values':['Dev']}])
    for instance in running_environment_instances:
        id=instance.id        
        stopped_list.append(ec2.instances.filter(InstanceIds=[id]).stop())
    return stopped_list


# Terminate all ec2 instances
def termin_ec2(ec2Obj):
    ''' This fn needs ec2 obj as argument and it terminates all instance found in the acccount and returns response list'''
    terminate_ec2 = []
    get_response = ec2Obj.describe_instances()
    for resource in get_response['Reservations']:
        for instance in resource['Instances']:
            terminate_ec2.append(instance['InstanceId'])
    list_termin_ec2 = ec2Obj.terminate_instances(InstanceIds=(terminate_ec2))
    return list_termin_ec2

# print("Terminated EC2 Instance list : ",list_termin_ec2)
#call the fn

#Code to list the running ec2 instances
def list_running_instances(ec2):
    '''Start the stopped ec2 instances'''
    running_list = []
    running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Environment','Values':['Dev']}])
    #running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']},{'Name': 'tag:Environment','Values':['Dev']}])
    for instance in running_instances:
        id=instance.id        
        running_instances.append(ec2.instances.filter(InstanceIds=[id]).running())
    return running_instances

#get started here to select what operations to be performed
count = 0
clr_scrn()
userinput = int(input("Estimated operation : "))
print("================= Welcome to EC2 Operations(Create,Stop,Start and Terminate EC2) ================")
while count < userinput:
    print("if we have count < userinput",count <= userinput)
    user_operations = int(input("\n To Create an EC2 Instance enter (1)\n To Stop Instances, enter (2)\n To Start enter (3)\n To List (4)\n To Terminate (5) : "))
    if user_operations == 1:
        get_min = int(input("whats the minimum no of EC2 instance : "))
        get_max = int(input("Whats the maximum no of EC2 Instance : "))
        get_imageid = str(input("Input your imageid : ")) #(amazon linux ami-id) ami-09d3b3274b6c5d4aa for t2.micro 
        get_instancetype = str(input("Input your Instance Type : "))
        get_created_ec2 = create_ec2(getObj_ec2,get_min,get_max,get_imageid,get_instancetype)
        print("List of Created Instances : ")
        for instance in get_created_ec2:
            print(f"Instance ID : {instance['InstanceId']} , Type : {instance['InstanceType']}")
        
    elif user_operations == 2:         
        get_stopped_list = stopped_environment_instances(stop_ec2) #To stop the instances
        print("Get the response : ",get_stopped_list) 
    elif user_operations == 3:
        get_starting_list = starting_instances(start_ec2) # To start the instances
        print("Response : ",get_starting_list)
    elif user_operations == 4:
        get_running_list = list_running_instances(list_instances) # To list the running instances
        print("Response : ",get_running_list)
    elif user_operations == 5:
        terminated_ec2 =termin_ec2(terminate_ec2)
        print("Get the response : ",terminated_ec2)
    userinput -= 1
            



    
