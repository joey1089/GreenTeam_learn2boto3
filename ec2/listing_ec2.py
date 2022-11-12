import boto3



ec2 = boto3.client('ec2')

response = ec2.describe_instances()

reservations = response['Reservations']

# print(reservations)

for reservation in reservations:
    instances = reservation['Instances']

    for instance in instances:
        print(instance['InstanceId'], instance['ImageId'])
        
    # for tag in tags.ec2():
    #     print(tag['key'],tag['value'])
        


# resource_ec2 = boto3.client('ec2')
# resource_ec2 = boto3.resource('ec2')


# response = resource_ec2.describe_instances()

# print(response)
# for i in resource_ec2.instances.all():
#     print(resource_ec2['Name'])

# for i in resource_ec2.instances.all():
#     print(resource_ec2['Name'])

    # if i.state['Name'] == 'stopped':

    #     i.start()