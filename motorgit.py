import click
import GithubHelper
import Constants

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

if __name__ == "__main__":
    motorgit()