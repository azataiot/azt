import click
from pyfiglet import Figlet


@click.group()
def cli():
    pass


@click.command()
def init():
    click.secho('init')


cli.add_command(init)
