import boto3



create_ec2 = boto3.client('ec2')
get_response = create_ec2.run_instances(ImageId='ami-09d3b3274b6c5d4aa',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName= 'GreenTeam_week14_Project',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Dev_Test01 Server'},
                {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
for _ in get_response['Instances']:
    print(f"Instance ID Created is :{(_['InstanceId']} Instance Type Created is : {_['InstanceType'])}")