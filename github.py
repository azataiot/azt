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


def git():
    """
    TODO:
    2. Check the user configurations of git repository.
    3. [TOC] don't work in github, so change something with hand.
    :return:
    """
    # Check git repository existence
    cmd = ['ls', '-a']
    console_out = subprocess.check_output(cmd)
    if console_out.decode('utf-8').find('.git') != -1:
        os.system('git add .')
        console_out2 = subprocess.check_output(['git', 'status'])
        if console_out2.decode('utf-8').find('Changes to be committed:') != -1:
            print('We have to commit something...')
            messages = []
            for each in console_out2.decode('utf-8').strip().strip(' ').strip('\t').split('\n'):
                if each.startswith('\tmodified') or each.startswith('\tdeleted') or each.startswith('\tnew file'):
                    messages.append(codecs.escape_decode(each.strip('\t'))[0].decode('utf-8'))
            comment_message = ','.join(messages)
            os.system(f'git commit -m "{comment_message}"')
            print('Pushing changes to Github')
            os.system('git push origin master')
            exit(0)
            # exit after pushing changes to Github.
        else:
            exit('Nothing to commit')
    else:
        exit('Not a valid git repository')


# 1. remove the old folders
click.secho("Removing the old folders: ")
os.system('rm -rf build')
os.system('rm -rf dist')
# 2. run the pyinstaller
click.secho('Running Pyinstaller for the azt.py file: ')
os.system('pyinstaller azt.py --onefile')
# 3. update the git
click.secho('Updating the projcet to the Github')
git()
