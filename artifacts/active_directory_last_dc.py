import os
import glob
from CoreFoundation import CFPreferencesCopyAppValue

factoid = 'active_directory_last_dc'

def fact():
    '''Returns the last used domain controller'''

    result = 'None'
    domain = None
    plist = None

    try:
        plist = glob.glob('/Library/Preferences/OpenDirectory/DynamicData/Active Directory/*.plist')[0]
    except IndexError:
        pass
    if plist and os.path.exists(plist):
        last_used_servers = CFPreferencesCopyAppValue('last used servers', plist)
        for k in last_used_servers.keys():
            if 'Global Catalog' not in k:
                domain = k
                break
        if domain:
            result = last_used_servers[domain]['host']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
