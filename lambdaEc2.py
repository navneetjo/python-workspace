import _json
import boto
import pprint
import json
import boto3
from aws_account_config import aws_account

from pprint import pprint

access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
pprint("access key : " + access_key)
pprint("secret key : " + secret_key)
region = 'us-east-1'
ec2 = boto3.client('ec2', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)


# following should be valid instance id
instances = ['i-0750283d8daa4874c']

status = ec2.describe_instances(InstanceIds=instances)
pprint("Current status of Instance is : " + str(status['Reservations'][0]['Instances'][0]['State']['Name']))
pprint("Instance Name is  : " + str(status['Reservations'][0]['Instances'][0]['Tags'][0]['Value']))


#check whether instance is running, if running shut down
if status['Reservations'][0]['Instances'][0]['State']['Name'] == "running":
    ec2.stop_instances(InstanceIds=instances)
    pprint("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is shutting down")

elif status['Reservations'][0]['Instances'][0]['State']['Name'] == "stopped":
    ec2.start_instances(InstanceIds=instances)
    pprint("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is starting")
else:
    pprint("Instance is terminated/pending")

