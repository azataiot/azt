import click
from pyfiglet import Figlet
import subprocess
import pkg_resources

azt_copyright = '❤ Azat Artificial Intelligence, LLP\n...Science and Technology Park of...\nAl-Farabi Kazakh National University'
update_message = ''


@click.command()
@click.version_option()
def cli():
    f = Figlet()
    azt_welcome = f.renderText('AzatAI')
    # subprocess.run(['pip', 'install', '--upgrade', 'azt'])
    click.secho(azt_welcome, fg='blue')
    click.echo(azt_copyright)
