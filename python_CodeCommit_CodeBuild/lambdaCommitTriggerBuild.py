import boto3
from pprint import pprint

# THIS FILE IS BELONG TO AWS LAMBDA FUNCTION ec2instanceLambda


# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
# code build trigger 'pythonFlaskExample' job

region = 'us-east-1'


def lambda_handler(event, context):
    codeBuild = boto3.client('codebuild', region_name=region)
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
