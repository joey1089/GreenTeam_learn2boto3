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

    
if __name__ == "__main__":
    get_stopped_list = stopped_environment_instances(ec2)
    # if get_stopped_list != []:
    #     print("List of stopped instances : ", get_stopped_list)




#[[{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-08e284fb6a4f5fb26', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': '034d2bfa-5dc2-4fce-b39f-482e5f822005', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '034d2bfa-5dc2-4fce-b39f-482e5f822005', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '579', 'date': 'Sun, 13 Nov 2022 21:14:21 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}], [{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-0df9fc16c06cddec6', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': 'fc9e9605-61c0-468e-9dfb-c031b40a346d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'fc9e9605-61c0-468e-9dfb-c031b40a346d', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '579', 'date': 'Sun, 13 Nov 2022 21:14:22 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}], [{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-05dca43b1bda7429d', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': '065c6c33-54af-4c0c-8181-03eba98ff1bf', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '065c6c33-54af-4c0c-8181-03eba98ff1bf', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '579', 'date': 'Sun, 13 Nov 2022 21:14:23 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}]]