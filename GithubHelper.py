from github import Github
from github import Auth
import Constants
import CommandHelper
import CredentialsHelper
import os

def createNewRepo(folderName, privateRepo):
    user = getGithubUser()
    folderName = getFolderName(folderName)
    user.create_repo(
        name = folderName,
        private = privateRepo
    )
    initializeNewRepo(folderName)
    updateRepo(commitMessage='Initial Commit')

def getFolderName(folderNameFromArgs):
    if not folderNameFromArgs:
        folderName = getFolderNameCWD()
    else:
        folderName = folderNameFromArgs.replace(" ", "-")
    return folderName

def getFolderNameCWD():
    cwd = os.path.basename(os.getcwd())
    return cwd.replace(" ", "-")

def updateRepo(commitMessage = 'Motorgit Commit', branchName = 'main'):
    gitAddAll()
    gitCommit(commitMessage)
    gitPush(branchName)

def getGithubUser():
    accessToken = CredentialsHelper.getGithubAccessToken()
    auth = Auth.Token(accessToken)
    g = Github(auth = auth)
    user = g.get_user()
    return user

def initializeNewRepo(folderName):
    gitInit()
    gitMain()
    gitUserName()
    gitUserEmail()
    gitAddRemote(folderName)

def addFilesAndPush(branchName):
    gitAddAll()
    gitCommit()
    gitPush(branchName)   

def gitInit():
    CommandHelper.executeCommandAndEchoOutput('git init')

def gitMain():
    CommandHelper.executeCommandAndEchoOutput('git branch -M main')

def gitUserName():
    CommandHelper.executeCommandAndEchoOutput(f'git config user.name {CredentialsHelper.getGithubUserName()}')

def gitUserEmail():
    CommandHelper.executeCommandAndEchoOutput(f'git config user.email {CredentialsHelper.getGithubUserEmail()}')

def gitAddAll():
    CommandHelper.executeCommandAndEchoOutput('git add .')

def gitCommit(commitMessage):
    CommandHelper.executeCommandAndEchoOutput(f'git commit -m \'{commitMessage}\'')

def gitAddRemote(folderName):
    CommandHelper.executeCommandAndEchoOutput(f"git remote add origin git@github.com:{CredentialsHelper.getGithubUserName()}/{folderName}.git")

def gitPush(branchName):
    CommandHelper.executeCommandAndEchoOutput(f"git push -u origin {branchName}")