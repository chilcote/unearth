import os
import subprocess

factoid = 'nodejs_version'

def fact():
    '''Returns the Node.js version if installed'''
    version = 'None'
    binary = '/usr/local/bin/node'
    if os.path.exists(binary):
        try:
            cmd = [binary, '--version']
            proc = subprocess.check_output(cmd)
            version = proc[1:].strip()
        except:
            pass

    return {factoid: version}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
