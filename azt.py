import click
from packages import branding, github
import settings


# Start the CLI here.
@click.group()
def cli():
    pass


@cli.command()  # @cli, not @click!
def git():
    click.secho('Running the ~azt Github utils:..', fg='blue')
    github.git()
    click.secho('~azt:Done!', bg='white', fg='green')


if __name__ == '__main__':
    branding.run()
    cli()
