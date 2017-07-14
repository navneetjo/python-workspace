import boto3

from aws_account_config import aws_account

from pprint import pprint

# code build trigger 'pythonFlaskExample' job
access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
region = 'us-east-1'

codeBuild = boto3.client('codebuild', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)

listProjects = codeBuild.list_projects()
for project in listProjects['projects']:
    pprint("Project Name : " + str(project))
    if project == 'pythonFlaskExample':
        print("I am here")
        startBuildInfo = codeBuild.start_build(projectName=project, artifactsOverride={'type': 'NO_ARTIFACTS'},
                                               environmentVariablesOverride=[
                                  {
                                      'name': 'string',
                                      'value': 'string'
                                      }
                                  ])
        pprint("Build Starting Information : " + str(startBuildInfo))
# Last builds id of every project
    buildId = codeBuild.list_builds_for_project(projectName=project)
    pprint("Project Information : " + str(buildId['ids'][0]))
