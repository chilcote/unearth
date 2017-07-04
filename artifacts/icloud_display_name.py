import os
from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = 'icloud_display_name'

def fact():
    '''Returns the icloud display name'''
    result = None

    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    plist = '/Users/%s/Library/Preferences/MobileMeAccounts.plist' % console_user
    if os.path.exists(plist):
        d = CFPreferencesCopyAppValue('Accounts', plist)
        result = d[0]['DisplayName'] if d else False

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
