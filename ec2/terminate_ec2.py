# Here we terminate all the ec2 instances that's in the account
import boto3
resource_ec2 = boto3.client('ec2')

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
terminated_ec2 =termin_ec2(resource_ec2)
print(terminated_ec2)
#{'TerminatingInstances': [{'CurrentState': {'Code': 48, 'Name': 'terminated'}, 'InstanceId': 'i-0a103e7cbd33971c0', 'PreviousState': {'Code': 80, 'Name': 'stopped'}}, {'CurrentState': {'Code': 32, 'Name': 'shutting-down'}, 'InstanceId': 'i-028f5cfd6201270c6', 'PreviousState': {'Code': 16, 'Name': 'running'}}, {'CurrentState': {'Code': 48, 'Name': 'terminated'}, 'InstanceId': 'i-0f51e9958e34386d1', 'PreviousState': {'Code': 80, 'Name': 'stopped'}}, {'CurrentState': {'Code': 48, 'Name': 'terminated'}, 'InstanceId': 'i-0d6f09b6e5a2f2cb2', 'PreviousState': {'Code': 80, 'Name': 'stopped'}}, {'CurrentState': {'Code': 32, 'Name': 'shutting-down'}, 'InstanceId': 'i-0643686638a7812e6', 'PreviousState': {'Code': 16, 'Name': 'running'}}, {'CurrentState': {'Code': 32, 'Name': 'shutting-down'}, 'InstanceId': 'i-0f1aa9df10579570d', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': '62442cf7-b3fe-4f46-969c-364c397ffa30', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '62442cf7-b3fe-4f46-969c-364c397ffa30', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'transfer-encoding': 'chunked', 'date': 'Mon, 14 Nov 2022 02:32:49 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}