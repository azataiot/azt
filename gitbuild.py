# -*- coding: utf-8 -*-
# run the Pyinstaller and then git push to the github.
from __future__ import print_function

import os
import os
import sys
import glob
import subprocess
import codecs
import click
from packages import github

# 1. remove the old folders
click.secho("Removing the old folders: ")
os.system('rm -rf build')
os.system('rm -rf dist')
# 2. run the pyinstaller
click.secho('Running Pyinstaller for the azt.py file: ')
os.system('pyinstaller azt.py --onefile')
# 3. update the git
click.secho('Updating the projcet to the Github')
github.git()
