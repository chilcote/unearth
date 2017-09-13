import os
import datetime
import plistlib

factoid = 'wifi_known_networks'

def fact():
    '''Returns the wifi ssid of the Mac'''

    result = {}
    plist = '/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist'

    if os.path.exists(plist):
        l = plistlib.readPlist(plist)["KnownNetworks"]

    for i in l:
        d = {}
        wifi = l['{0}'.format(i)]
        # Ensure SSID is converted to utf and ignore characters it could fail
        # on.
        ssid = wifi['SSID'].data.decode('utf-8', 'ignore')
        d['security_type'] = wifi['SecurityType']
        d['personal_hotspot'] = wifi['PersonalHotspot']
        if wifi.get('LastConnected', None):
            d['last_connected'] = wifi['LastConnected'].strftime('%Y-%m-%dT%H:%M:%S')
            #d['last_connected'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(wifi['LastConnected']))
        result[ssid] = d

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
