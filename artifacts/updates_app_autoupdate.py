#!/usr/bin/env python

from CoreFoundation import (CFPreferencesCopyValue, kCFPreferencesAnyHost, 
kCFPreferencesAnyUser)

factoid = 'updates_app_autoupdate'

def fact():
    '''Returns the status of automatic updates to MAS apps'''
    status = "disabled"
    pref = CFPreferencesCopyValue('AutoUpdate',
                    '/Library/Preferences/com.apple.commerce.plist',
                    kCFPreferencesAnyUser, kCFPreferencesAnyHost)
    if pref:
        status = "enabled"

    return {factoid: status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
