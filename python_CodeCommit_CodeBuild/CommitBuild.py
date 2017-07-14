import boto3

from aws_account_config import aws_account

from pprint import pprint

access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
region = 'us-east-1'

codeBuild = boto3.client('codebuild', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)

listProjects = codeBuild.list_projects()
for project in listProjects['projects']:
    pprint("Project Name : " + str(project))

# Last builds id of every project
    buildId = codeBuild.list_builds_for_project(projectName=project)
    pprint("Project Information : " + str(buildId['ids'][0]))
    lastId = buildId['ids'][0].split(':')[1]
    pprint("Id is : " + str(lastId))

# check last build status of every project
    buildStatus = codeBuild.batch_get_builds(ids=[buildId['ids'][0]])
    pprint("Build Status : " + buildStatus['builds'][0]['phases'][0]['phaseStatus'])



"""
    # project Information
    projectInfo = codeBuild.batch_get_builds(names=[project])
    pprint("Information : " + str(projectInfo))
"""

# 1. start a specific project build
# 2. current status of all the projects
