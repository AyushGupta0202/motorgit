import os
import warnings
if os.environ.get("_MOTORGIT_COMPLETE"):
    warnings.filterwarnings("ignore")
import click
import GithubHelper
import Constants
import CredentialsHelper

@click.group()
@click.version_option(Constants.version, '--version', '-v', message='Motorgit %(version)s')
def motorgit():
    """Automate git repository creation"""
    pass

@motorgit.command('anotherMethod')
@click.option('--name', '-n', 'Name', default='', required=False, help='Test method')
def anotherMethod(Name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(Name)

@motorgit.command('createNewRepo')
@click.option('--name', '-n', 'folderName', default='', required=False, help="Custom folder name, if not given it will take the name of the directory")
@click.option('--private', '-p', 'privateRepo', default=False, required=False, help="Creates repository as private if True")
def createNewRepo(folderName, privateRepo):
    """Create new repository at remote."""
    GithubHelper.createNewRepo(folderName, privateRepo)

@motorgit.command('updateRepo')
@click.option('--message', '-m', 'commitMessage', default='Motorgit Commit', required=False, help="Add a Commit Message")
@click.option('--branch', '-b', 'branchName', default='main', required=False, help="Set remote branch name")
def updateRepo(commitMessage, branchName):
   """Update existing repository at remote."""
   GithubHelper.updateRepo(commitMessage, branchName)

@motorgit.command('setup')
@click.option('--non-interactive', is_flag=True, help="Use environment variables instead of prompting")
def setup(non_interactive):
    """Set up GitHub credentials.
    
    This command will guide you through setting up your GitHub credentials
    securely using your system's credential store.
    """
    interactive = not non_interactive
    if CredentialsHelper.setupCredentials(interactive):
        click.echo("GitHub credentials setup successfully!")
    else:
        click.echo("Failed to setup GitHub credentials.")

@motorgit.command('login')
def login():
    """Store GitHub credentials securely.
    
    This command will prompt for your GitHub username, email, and access token
    and store them securely.
    """
    if CredentialsHelper.setupCredentials(interactive=True):
        click.echo("GitHub credentials stored successfully!")
    else:
        click.echo("Failed to store GitHub credentials.")

@motorgit.command('logout')
def logout():
    """Remove stored GitHub credentials.
    
    This will remove all credentials stored by Motorgit.
    """
    if CredentialsHelper.removeCredentials():
        click.echo("GitHub credentials removed successfully!")
    else:
        click.echo("Failed to remove GitHub credentials.")

@motorgit.command('config')
@click.argument('key', required=False)
@click.argument('value', required=False)
@click.option('--list', '-l', is_flag=True, help="List all configuration values")
def config(key, value, list):
    """View or update configuration.
    
    Without arguments, displays all configuration.
    With KEY only, displays that configuration value.
    With KEY and VALUE, sets that configuration.
    """
    from ConfigHelper import ConfigHelper
    config_helper = ConfigHelper()
    
    if list or (not key and not value):
        # Display all config
        config = config_helper.load_config()
        for k, v in config.items():
            if k != "credential_store":  # Don't show sensitive values
                click.echo(f"{k}: {v}")
            else:
                click.echo(f"{k}: {v}")
    elif key and not value:
        # Display specific config
        value = config_helper.get_config(key)
        if value is not None:
            click.echo(f"{key}: {value}")
        else:
            click.echo(f"Configuration key '{key}' not found.")
    elif key and value:
        # Set config
        if config_helper.update_config(key, value):
            click.echo(f"Updated {key} to {value}")
        else:
            click.echo(f"Failed to update configuration.")

if __name__ == "__main__":
    motorgit()