import os
from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'java_vendor'

def fact():
    '''Returns the java vendor (apple or oracle)'''
    result = None

    plist = '/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Info.plist'
    if os.path.exists(plist):
        result = CFPreferencesCopyAppValue('CFBundleIdentifier', plist).split('.')[1]

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
