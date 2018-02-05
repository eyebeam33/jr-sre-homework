#!/cygdrive/c/Python35/python.exe
# relies on default VPC existing

import boto3
import datetime
import time

ec2 = boto3.client('ec2')

response = ec2.run_instances(ImageId='ami-7d3dc51d',InstanceType='t2.micro',MaxCount=1,MinCount=1,SubnetId='subnet-9123f9cb')
instance_id = response['Instances'][0]['InstanceId']

I = ec2.describe_instances(InstanceIds=[instance_id])

launch_time = I['Reservations'][0]['Instances'][0]['LaunchTime']
state_name  = I['Reservations'][0]['Instances'][0]['State']['Name']

print (launch_time, instance_id, state_name)

time.sleep(300)

ec2.terminate_instances(InstanceIds=[instance_id])
