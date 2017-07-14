import boto3
import botocore

def lambda_handler(event, context):
    rds = boto3.client('rds')
    rds.stop_db_instance(DBInstanceIdentifier='stop_db_instance')
