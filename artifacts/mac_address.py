import imp
import os
import subprocess
import sys
from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'mac_address'

def primary_interface():
    '''Returns the primary interface of this Mac'''
    primary_interface = None
    net_config = SCDynamicStoreCreate(None, "net", None, None)
    try:
        states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
        primary_interface = states['PrimaryInterface']
    except TypeError:
        pass

    return primary_interface

def fact():
    '''Returns the mac address of this Mac'''
    mac_address = None
    iface = primary_interface()
    if iface:
        try:
            proc = subprocess.Popen(['/usr/sbin/networksetup',
                                    '-getmacaddress',
                                    iface],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = proc.communicate()
            mac_address = stdout.strip().split(' ')[2]
        except (IOError, OSError):
            pass

    return {factoid: mac_address}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
