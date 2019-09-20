import click
from pyfiglet import Figlet


azt_copyright = '©Azat Artificial Intelligence, LLP\nAl-Farabi Kazakh National University'


@click.command()
@click.version_option()
def cli():
    f = Figlet()
    azt_welcome = f.renderText('AzatAI')
    click.secho(azt_welcome, fg='blue')
    click.echo(azt_copyright)
