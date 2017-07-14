import boto3
from aws_account_config import aws_account

from pprint import pprint

access_key = aws_account["access_key_id"]
secret_key = aws_account["secret_access_key"]
region = 'us-east-1'

codeCommit = boto3.client('codecommit', aws_secret_access_key=secret_key, aws_access_key_id=access_key, region_name=region)


listRepos = codeCommit.list_repositories()
# pprint("List of repositories :" + str(listRepos['repositories']) + '\n')


"""
# List of repositories
for repo in listRepos['repositories']:
    pprint("List of repositories : " + str(repo['repositoryName']))

"""
# this code will print the last commit information for every repository default branch
for repo in listRepos['repositories']:
    pprint("Name of Repository : " + str(repo['repositoryName']))
    repoInfo = codeCommit.get_repository(repositoryName=repo['repositoryName'])
    pprint("Default Branch : " + str(repoInfo['repositoryMetadata']['defaultBranch']))
    commitId = codeCommit.get_branch(repositoryName=repo['repositoryName'],
                                     branchName=repoInfo['repositoryMetadata']['defaultBranch'])
    pprint("commit id: " + str(commitId['branch']['commitId']))
    commitInfo = codeCommit.get_commit(repositoryName=repo['repositoryName'], commitId=commitId['branch']['commitId'])
    pprint("Commit Information : " + str(commitInfo['commit']))
    pprint("Commit Information : " + str(commitInfo['commit']['message']))
    pprint("Commit Information : " + str(commitInfo['commit']['author']['name']))
    pprint("Commit Information : " + str(commitInfo['commit']['author']['email']))
    pprint("Commit Information : " + str(commitInfo['commit']['committer']['date']))

"""
    pprint("branches information : " + str(repoName['repositoryMetadata']['defaultBranch']))
    branch = repoName['repositoryMetadata']['defaultBranch']
    pprint("Branch is: " + branch)
    commitId = codeCommit.get_branch(repositoryName=repoName,branchName=branch)
    pprint("Commit id : " + commitId)



        for branch in branches['branch']:
        pprint("Branch Name : " + branch['branchName'])
        pprint("Commit-Id : " + branch['branch']['commitId'])
    # commits = codeCommit.get_commit(repositoryName=repo['repositoryName'],commitId='branch['branches'])
    # pprint("Commits : " + commits)
"""