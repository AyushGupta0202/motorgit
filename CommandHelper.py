import subprocess
import click

def executeSubprocessCommand(command):
    status = subprocess.getstatusoutput(command)
    if (status[0] == 0):
        return status[1]
    click.echo(status[1])
    return "-1"

def executeCommandAndEchoOutput(command):
    status = executeSubprocessCommand(command)