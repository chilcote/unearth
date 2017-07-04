import os
import plistlib

factoid = 'xprotect_version'

def fact():
    '''Returns the xprotect version'''

    result = None
    path = '/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist'

    if os.path.exists(path):
        with open(path, 'r') as f:
            d = plistlib.readPlist(path)
        result = int(d['Version'])

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
