from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'updates_check_status'

def fact():
    '''
    Reports the overall status of automatic update checking for OS X updates,
    App Store app updates, and Gatekeeper and XProtect configurations
    '''
    status = "disabled"
    pref = CFPreferencesCopyAppValue('AutomaticCheckEnabled',
                    '/Library/Preferences/com.apple.SoftwareUpdate')
    if pref:
        status = "enabled"

    return {factoid: status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]