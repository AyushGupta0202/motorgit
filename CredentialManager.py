import os
import keyring
import getpass
import Constants
from ConfigHelper import ConfigHelper

class CredentialManager:
    """Manages secure storage and retrieval of GitHub credentials"""
    
    SERVICE_NAME = "motorgit"
    
    def __init__(self):
        self.config_helper = ConfigHelper()
    
    def store_github_token(self, token):
        """Store GitHub access token in keyring"""
        try:
            keyring.set_password(
                self.SERVICE_NAME, 
                Constants.GITHUB_ACCESSTOKEN, 
                token
            )
            return True
        except Exception as e:
            print(f"Error storing token in keyring: {e}")
            return False
    
    def get_github_token(self):
        """Get GitHub access token from keyring or environment"""
        # First try keyring
        try:
            token = keyring.get_password(
                self.SERVICE_NAME, 
                Constants.GITHUB_ACCESSTOKEN
            )
            if token:
                return token
        except Exception as e:
            print(f"Error retrieving token from keyring: {e}")
        
        # Fall back to environment variable
        try:
            return os.environ.get(Constants.GITHUB_ACCESSTOKEN)
        except:
            return None
    
    def store_github_username(self, username):
        """Store GitHub username in config"""
        return self.config_helper.update_config("github_username", username)
    
    def get_github_username(self):
        """Get GitHub username from config or environment"""
        # First try config
        username = self.config_helper.get_config("github_username")
        if username:
            return username
        
        # Fall back to environment variable
        return os.environ.get(Constants.GITHUB_USERNAME)
    
    def store_github_email(self, email):
        """Store GitHub email in config"""
        return self.config_helper.update_config("github_email", email)
    
    def get_github_email(self):
        """Get GitHub email from config or environment"""
        # First try config
        email = self.config_helper.get_config("github_email")
        if email:
            return email
        
        # Fall back to environment variable
        return os.environ.get(Constants.GITHUB_USEREMAIL)
    
    def remove_all_credentials(self):
        """Remove all stored credentials"""
        try:
            keyring.delete_password(self.SERVICE_NAME, Constants.GITHUB_ACCESSTOKEN)
        except:
            pass
        
        self.config_helper.update_config("github_username", "")
        self.config_helper.update_config("github_email", "")
        return True
    
    def setup_credentials(self, interactive=True):
        """Setup all GitHub credentials interactively or from environment"""
        if interactive:
            username = input("GitHub Username: ")
            email = input("GitHub Email: ")
            token = getpass.getpass("GitHub Access Token: ")
            
            self.store_github_username(username)
            self.store_github_email(email)
            self.store_github_token(token)
            
            print("Credentials saved successfully!")
            return True
        else:
            # Try to read from environment
            username = os.environ.get(Constants.GITHUB_USERNAME)
            email = os.environ.get(Constants.GITHUB_USEREMAIL)
            token = os.environ.get(Constants.GITHUB_ACCESSTOKEN)
            
            if username and email and token:
                self.store_github_username(username)
                self.store_github_email(email)
                self.store_github_token(token)
                return True
            else:
                print("Missing environment variables for GitHub credentials.")
                return False 