from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'updates_app_autoupdate'

def fact():
    '''Returns the status of automatic updates to MAS apps'''
    status = "disabled"
    pref = CFPreferencesCopyAppValue('AutoUpdate',
                    '/Library/Preferences/com.apple.commerce.plist')
    if pref:
        status = "enabled"

    return {factoid: status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]