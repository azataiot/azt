import click
from pyfiglet import Figlet

f = Figlet()
azt_welcome = f.renderText('AzatAI')


@click.command()
@click.version_option()
def cli():
    click.secho(azt_welcome, fg='blue')
