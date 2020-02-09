import codecs
import os
import sys
import subprocess


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
            sys.exit(0)
            # exit after pushing changes to Github.
        else:
            sys.exit('Nothing to commit')
    else:
        sys.exit('Not a valid git repository')
