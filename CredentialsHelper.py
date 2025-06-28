import os
import Constants
from CredentialManager import CredentialManager

# Create credential manager instance
_credential_manager = CredentialManager()

def getEnvironmentVariable(key):
    """Get a value from environment variables (legacy method)"""
    if key not in os.environ:
        raise Exception(f"{key} not present in Environment variables")
    return os.environ[key]

def getGithubAccessToken():
    """Get GitHub access token from credential manager or environment"""
    token = _credential_manager.get_github_token()
    if token:
        return token
    
    # Legacy fallback
    return getEnvironmentVariable(Constants.GITHUB_ACCESSTOKEN)

def getGithubUserName():
    """Get GitHub username from credential manager or environment"""
    username = _credential_manager.get_github_username()
    if username:
        return username
    
    # Legacy fallback
    return getEnvironmentVariable(Constants.GITHUB_USERNAME)

def getGithubUserEmail():
    """Get GitHub email from credential manager or environment"""
    email = _credential_manager.get_github_email()
    if email:
        return email
    
    # Legacy fallback
    return getEnvironmentVariable(Constants.GITHUB_USEREMAIL)

def setupCredentials(interactive=True):
    """Setup GitHub credentials"""
    return _credential_manager.setup_credentials(interactive)

def removeCredentials():
    """Remove stored credentials"""
    return _credential_manager.remove_all_credentials()