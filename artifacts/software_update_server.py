from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'software_update_server'

def fact():
    '''Returns the software update server'''
    sus = 'None'

    sus = CFPreferencesCopyAppValue('CatalogURL',
                    '/Library/Preferences/com.apple.SoftwareUpdate.plist')

    return {factoid: str(sus)}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
