from SystemConfiguration import (SCDynamicStoreCopyValue, SCDynamicStoreCreate,
                                 SCNetworkInterfaceCopyAll,
                                 SCNetworkInterfaceGetBSDName,
                                 SCNetworkInterfaceGetHardwareAddressString)

factoid = "mac_address"


def fact():
    """Returns the mac address of this Mac"""
    primary_MAC = "None"
    net_config = SCDynamicStoreCreate(None, "net", None, None)
    states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
    primary_interface = states["PrimaryInterface"]
    primary_devices = [
        x
        for x in SCNetworkInterfaceCopyAll()
        if SCNetworkInterfaceGetBSDName(x) == primary_interface
    ]
    if primary_devices:
        primary_MAC = SCNetworkInterfaceGetHardwareAddressString(primary_devices[0])
    return {factoid: primary_MAC}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
