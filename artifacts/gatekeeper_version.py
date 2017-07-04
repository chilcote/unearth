import os
from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'gatekeeper_version'

def fact():
    '''Returns the gatekeeper version'''
    plist = '/private/var/db/gkopaque.bundle/Contents/version.plist'
    if os.path.exists(plist):
        result = CFPreferencesCopyAppValue('CFBundleShortVersionString', plist)

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
