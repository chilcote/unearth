from SystemConfiguration import SCNetworkInterfaceCopyAll, \
                                SCNetworkInterfaceGetLocalizedDisplayName

factoid = 'network_services'

def fact():
    '''Return the value of the computername of this Mac'''
    network_interfaces = SCNetworkInterfaceCopyAll()
    interfaces = []
    for interface in network_interfaces:
        interfaces.append(SCNetworkInterfaceGetLocalizedDisplayName(interface))

    return {factoid: interfaces}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
