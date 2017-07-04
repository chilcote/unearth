import imp
import os
import sys
from SystemConfiguration import SCNetworkInterfaceGetLocalizedDisplayName, \
                                SCNetworkInterfaceGetBSDName, \
                                SCNetworkInterfaceGetHardwareAddressString, \
                                SCNetworkInterfaceCopyAll

factoid = 'wifi_interface'

def interfaces():
    '''Returns a list of all network interface names'''
    network_interfaces = SCNetworkInterfaceCopyAll()
    interfaces = {}
    for interface in network_interfaces:
        interfaces[SCNetworkInterfaceGetLocalizedDisplayName(interface)] = (
            SCNetworkInterfaceGetBSDName(interface),
            SCNetworkInterfaceGetHardwareAddressString(interface)
            )
    return interfaces

def fact():
    '''Returns wifi interface'''
    wifi_interface = None
    interface = interfaces()

    try:
        wifi_interface = interface['Wi-Fi'][0]
    except KeyError:
        pass

    return {factoid: wifi_interface}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
