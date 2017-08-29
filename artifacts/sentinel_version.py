import os
from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'sentinel_version'

def fact():
    '''Returns the sentinel version'''
    version = 'None'
    plist = '/Library/Sentinel/sentinel-agent.bundle/Contents/Info.plist'
    if os.path.exists(plist):
        version = CFPreferencesCopyAppValue('CFBundleShortVersionString', plist)

    return {factoid: version}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
