import subprocess
import click

def executeSubprocessCommand(command):
    return subprocess.getstatusoutput(command)

def executeCommandAndEchoOutput(command):
    status = executeSubprocessCommand(command)
    click.echo(status)