import boto3

ec2 = boto3.resource('ec2', aws_access_key_id=<aws_access_key_id>,
                     aws_secret_access_key=<aws_secret_access_key>,
                     region_name='ap-south-1')

# create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.127/26')
