from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'updates_software_download'

def fact():
    '''Returns the status of automatic downloading of software updates'''
    status = "disabled"
    pref = CFPreferencesCopyAppValue('AutomaticDownload',
                    '/Library/Preferences/com.apple.SoftwareUpdate')
    if pref:
        status = "enabled"

    return {factoid: status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]