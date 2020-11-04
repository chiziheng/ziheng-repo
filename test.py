# %%
import boto3
import botocore
session=boto3.Session(profile_name="default")

#%%
ec2 = session.client('ec2')
response = ec2.describe_key_pairs()
print(response['KeyPairs'])

#%%
ec2_re=session.resource(service_name="ec2")
ec2 = session.client('ec2')
for each_ins in ec2_re.instances.all():
    print(each_ins)
Test_Mysql_Instance=ec2_re.create_instances(
    MaxCount=1,
    MinCount=1,
    ImageId='ami-0f82752aa17ff8f5d',
    InstanceType='t1.micro',
    SecurityGroups=['Mysql instance security group'],
    KeyName="Mysql_instance_key"
)
# ec2_obj=boto3.resource("ec2")

#%%
import boto3
from botocore.exceptions import ClientError

session=boto3.Session(profile_name="default")
ec2 = session.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    response = ec2.create_security_group(GroupName='Mysql instance security group',
                                         Description='security group for Mysql instance',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)

try:
    response = ec2.create_security_group(GroupName='Mongodb instance security group',
                                         Description='security group for Mongodb instance',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)

#%%

#%%
sg_name_list=['Mysql instance security group','Mongodb instance security group']
response = ec2.describe_security_groups(
    Filters=[
        dict(Name='group-name', Values=sg_name_list)
    ]
)

sg_ids=[]
for i in range(len(response['SecurityGroups'])):
    group_id = response['SecurityGroups'][i]['GroupId']
    sg_ids.append(group_id)
print(sg_ids)
#%%
response = ec2.delete_security_group(GroupId='sg-01cd4c9241573aab0')
print('Security Group Deleted')