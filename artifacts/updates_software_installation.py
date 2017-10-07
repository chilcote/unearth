from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'updates_software_installation'

def fact():
    '''Returns the status of automatic installation of downloaded updates'''
    status = "disabled"
    pref = CFPreferencesCopyAppValue('AutoUpdateRestartRequired',
                    '/Library/Preferences/com.apple.commerce.plist')
    if pref:
        status = "enabled"

    return {factoid: status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]