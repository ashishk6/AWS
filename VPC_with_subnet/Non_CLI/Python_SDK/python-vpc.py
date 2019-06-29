import boto3

ec2 = boto3.resource('ec2',
                     region_name='ap-south-1')

# create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.64/26')

print(vpc.id)
# create subnet
subnet = ec2.create_subnet(CidrBlock='10.0.0.64/28', VpcId=vpc.id)
print(subnet.id)