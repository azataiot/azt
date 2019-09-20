import click

@click.group()
@click.version_option()
def cli():
    """ ~ Welcome to the Future!

    This is the first azt cli test, we gonna work on this hard staff maybe for a long while....
    """


@cli.group()
def install():
    """
    Install ~azt packages
    """


@install.command()
@click.argument('pkg')
def install_pkg(pkg):
    """
    Install an ~azt package from ~azt package index.
    """
    click.secho("Installing ~azt package:{}".format(pkg))

