import boto3

resource_ec2 = boto3.client("ec2")

responce = resource_ec2.create_ec2(
    {
        
    }
)