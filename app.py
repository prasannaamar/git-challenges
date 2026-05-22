import boto3

# Create EC2 client
ec2 = boto3.resource('ec2', region_name='us-east-1')

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.medium',
    KeyName='your-keypair-name',   # Replace with your key pair
    SecurityGroupIds=['sg-xxxxxxxx'],
    SubnetId='subnet-xxxxxxxx',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'key'
                }
            ]
        }
    ]
)

print("EC2 Instance Created!")
print("Instance ID:", instances[0].id)
