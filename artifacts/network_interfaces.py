from SystemConfiguration import (
    SCNetworkInterfaceCopyAll,
    SCNetworkInterfaceGetBSDName,
    SCNetworkInterfaceGetHardwareAddressString,
    SCNetworkInterfaceGetLocalizedDisplayName,
)

factoid = "network_interfaces"


def fact():
    """Returns a list of all network interface names"""
    network_interfaces = SCNetworkInterfaceCopyAll()
    interfaces = {}
    for interface in network_interfaces:
        interfaces[SCNetworkInterfaceGetLocalizedDisplayName(interface)] = (
            SCNetworkInterfaceGetBSDName(interface),
            SCNetworkInterfaceGetHardwareAddressString(interface),
        )

    return {factoid: str(interfaces)}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
