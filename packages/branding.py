from datetime import datetime
import click

AZATAI_TEXT = """
    _              _      _    ___ 
   / \    ______ _| |_   / \  |_ _|
  / _ \  |_  / _` | __| / _ \  | | 
 / ___ \  / / (_| | |_ / ___ \ | | 
/_/   \_\/___\__,_|\__/_/   \_\___|
"""

year_current = datetime.now().year
print(AZATAI_TEXT)
click.secho(f'© {year_current} Azat Artificial Intelligence', fg='blue')
click.secho(f"{' ' * 4}", nl=False)
click.secho('Build', fg='blue', nl=False)
click.secho('     ', nl=False, fg='blue')
click.secho('Design', nl=False, fg='red')
click.secho('     ', nl=False, fg='blue')
click.secho('Learn', fg='yellow', nl=False)
click.secho('     ', nl=False)
click.secho()
click.secho('https://azat.ai', nl=False)
click.secho('        ', nl=False)
click.secho('info@azat.ai')
