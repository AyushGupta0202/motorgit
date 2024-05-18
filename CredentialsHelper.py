import os
import Constants

def getEnvironmentVariable(key):
    if key not in os.environ:
        raise Exception(f"{key} not present in Environment variables")
    return os.environ[key]

def getGithubAccessToken():
    return getEnvironmentVariable(Constants.GITHUB_ACCESSTOKEN)

def getGithubUserName():
    return getEnvironmentVariable(Constants.GITHUB_USERNAME)

def getGithubUserEmail():
    return getEnvironmentVariable(Constants.GITHUB_USEREMAIL)