import boto3
import botocore
from pprint import pprint
import json
import pdb

from aws_access import aws_account

# THIS FILE IS BELONG TO AWS LAMBDA FUNCTION rds_lambda_start-instance

# Enter the region your instances are in, e.g. 'us-east-1'

region = 'us-east-1'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
pprint("access key : " + access_key)
pprint("secret key : " + secret_key)


rds = boto3.client('rds', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)
pprint("Version is {}".format(botocore.__version__))
rds.stop_db_instance(DBInstanceIdentifier='stop_db_instance')




