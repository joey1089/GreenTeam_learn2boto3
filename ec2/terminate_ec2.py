# Here we terminate the ec2 instances
import boto3

terminate_ec2 = []
resource_ec2 = boto3.client('ec2')
get_response = resource_ec2.describe_instances()
for resource in get_response['Reservations']:
    for instance in resource['Instances']:
        terminate_ec2.append(instance['InstanceId'])

list_termin_ec2 = resource_ec2.terminate_instances(InstanceIds=(terminate_ec2))
print("Terminated EC2 Instance list : ",list_termin_ec2)