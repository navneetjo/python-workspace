import json
import boto3
from aws_account_config import aws_account

from pprint import pprint

# method 1 for print the value of resource.json file
#with open('aws_account_config.json') as data_file:
#    data = json.load(data_file)
#pprint(data)

# method 2 for print the value of resource.json file
#config = json.loads(open('resource.json').read())
#pprint(config)
#pprint("aws access key " + str(config["aws_resource"][0]["aws_access_key_id"]))

# start ec2 instance
access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
pprint("access key : " + access_key)
pprint("secret key : " + secret_key)
region = 'us-east-1'
ec2 = boto3.client('ec2', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)


# following should be valid instance id
instances = ['i-0750283d8daa4874c']

'''
# start an instance
ec2.start_instances(InstanceIds=instances)
'''

# pprint("Instance Information" + str(instances['InstanceStatuses']))

status = ec2.describe_instances()
for s in status['Reservations']:
    for s1 in s['Instances']:
        pprint("Instance Name  : " + str(s1['Tags'][0]['Value']))
        pprint("Instance Id  : " + str(s1['InstanceId']) + " State : " + str(s1['State']['Name']))
        #shut-down instances which are running
        if str(s1['State']['Name']) == 'running':
            instId = s1['InstanceId']
            print("ID "+instId)
            ec2.stop_instances(InstanceIds=[instId])
            pprint("going to shutdown instance " + str(s1['Tags'][0]['Value']))

"""
#pprint("complete Object" + str(status))


# pprint("State  : "+str(status['Reservations'][0]['Instances'][0]['State']['Name']))
# pprint("Instance id  : "+str(status['Reservations'][0]['Instances'][0]['InstanceId']))

# pprint("state of instance is " + instances.state())

"""