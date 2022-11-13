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
    if get_stopped_list != []:
        print("List of stopped instances : ", get_stopped_list)




# [[{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-00ddf9129854b4434', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 
# 'ResponseMetadata': {'RequestId': '4719a095-5fc3-4578-aef4-f270efcb61fc', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4719a095-5fc3-4578-aef4-f270efcb61fc', 
# 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 
# 'content-length': '579', 'date': 'Sun, 13 Nov 2022 07:37:15 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}], 
# [{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-0c4e8885a1c48171b', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 
# 'ResponseMetadata': {'RequestId': 'b2f5fb3d-fea2-4b9f-bd11-cf59dee0c14c', 'HTTPStatusCode': 200, 
# 'HTTPHeaders': {'x-amzn-requestid': 'b2f5fb3d-fea2-4b9f-bd11-cf59dee0c14c', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; 
# includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '579', 'date': 'Sun, 13 Nov 2022 07:37:15 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}], 
# [{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-0cb4b6bb2d5f7f6ff', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 
# 'ResponseMetadata': {'RequestId': 'f0d7b116-923f-4e3a-966b-b5a7f960346f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'f0d7b116-923f-4e3a-966b-b5a7f960346f', 
# 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '579', 
# 'date': 'Sun, 13 Nov 2022 07:37:16 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}]]