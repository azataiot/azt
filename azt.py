import click
from packages import branding, github
import settings


# Start the CLI here.
@click.group()
def cli():
    pass


@cli.command()  # @cli, not @click!
def git():
    click.secho('Running the ~azt Github utils:..')
    github.git()


if __name__ == '__main__':
    branding.run()
    cli()
