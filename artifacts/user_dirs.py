import datetime
import plistlib
import subprocess
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = 'user_dirs'

def fact():
    '''Gets the home directories of all console users'''
    users = []
    homes = []

    excluded = ('root', 'daemon', 'nobody')
    cmd = ['/usr/bin/dscl', '.', 'list', '/Users']
    output = subprocess.check_output(cmd)
    for user in output.split():
        if user not in excluded and not user.startswith('_'):
            users.append(user)

    for user in users:
        cmd = ['/usr/bin/dscl', '-plist', '.', 'read', '/Users/' + user]
        output = subprocess.check_output(cmd)
        d = plistlib.readPlistFromString(output)
        homes.append(d['dsAttrTypeStandard:NFSHomeDirectory'][0])

    return {factoid: homes}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
