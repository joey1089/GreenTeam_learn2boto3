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

    
if __name__ == "__main__":
    get_starting_list = starting_instances(ec2)
