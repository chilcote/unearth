from SystemConfiguration import SCNetworkInterfaceGetLocalizedDisplayName, \
                                SCNetworkInterfaceGetBSDName, \
                                SCNetworkInterfaceGetHardwareAddressString, \
                                SCNetworkInterfaceCopyAll

factoid = 'wifi_macaddress'

def interfaces():
    '''Returns a list of all network interface names'''
    interfaces = {}
    network_interfaces = SCNetworkInterfaceCopyAll()
    for interface in network_interfaces:
        interfaces[SCNetworkInterfaceGetLocalizedDisplayName(interface)] = (
            SCNetworkInterfaceGetBSDName(interface),
            SCNetworkInterfaceGetHardwareAddressString(interface)
            )
    return interfaces

def fact():
    '''Returns the Wi-Fi MAC address'''
    wifi_macaddress = None
    interface = interfaces()
    try:
        wifi_macaddress = interface['Wi-Fi'][1]
    except KeyError:
        pass
    return {factoid: wifi_macaddress}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
