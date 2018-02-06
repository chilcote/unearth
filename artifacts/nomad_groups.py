from SystemConfiguration import SCDynamicStoreCopyConsoleUser
from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'nomad_groups'

def fact():
    '''Gets the AD groups from the nomad plist'''
    result = ''

    username = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    if username:
        result = CFPreferencesCopyAppValue('Groups',
                    '/Users/%s/Library/Preferences/com.trusourcelabs.NoMAD.plist' % username)

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % ','.join(fact()[factoid])
