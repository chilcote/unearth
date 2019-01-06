import datetime
import plistlib
import subprocess
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = 'password_age'

def fact():
    '''Gets the age of last password change'''
    password_age = None
    password_changed = False

    # for 10.10+ or non-migrated accounts
    username = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    if username:
        task = subprocess.check_output(['/usr/bin/dscl', '.', 'read', 'Users/' + username, 'accountPolicyData'])
        plist = plistlib.readPlistFromString('\n'.join(task.split()[1:]))
        if 'passwordLastSetTime' in plist.keys():
            password_changed = datetime.datetime.utcfromtimestamp(plist['passwordLastSetTime']).date()
        else:
            # for 10.9.x and lower, or migrated accounts
            task = subprocess.Popen(['/usr/bin/dscl', '.', 'read', 'Users/' + username, 'PasswordPolicyOptions'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (out, err) = task.communicate()
            if not err:
                plist = plistlib.readPlistFromString('\n'.join(out.split()[1:]))
                if 'passwordLastSetTime' in plist.keys():
                    password_changed = plist['passwordLastSetTime'].date()

        if password_changed:
            today = datetime.datetime.utcnow().date()
            password_age = (today - password_changed).days
        else:
            password_age =  'Undetermined'

    return {factoid: password_age}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
