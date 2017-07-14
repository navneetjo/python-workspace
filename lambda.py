import boto3

# THIS FILE IS BELONG TO AWS LAMBDA FUNCTION ec2instanceLambda
# Enter the region your instances are in, e.g. 'us-east-1'

region = 'us-east-1'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

instances = ['i-0750283d8daa4874c']


def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    status = ec2.describe_instances(InstanceIds=instances)

    if status['Reservations'][0]['Instances'][0]['State']['Name'] == "running":
        ec2.stop_instances(InstanceIds=instances)
        print("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is shutting down")

    elif status['Reservations'][0]['Instances'][0]['State']['Name'] == "stopped":
        ec2.start_instances(InstanceIds=instances)
        print("Instance " + status['Reservations'][0]['Instances'][0]['Tags'][0]['Value'] + " is starting")
    else:
        print("Instance is terminated/pending")


