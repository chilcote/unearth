from SystemConfiguration import (
    SCDynamicStoreCreate,
    SCDynamicStoreCopyValue,
    SCNetworkInterfaceCopyAll,
    SCNetworkInterfaceGetBSDName,
    SCNetworkInterfaceGetHardwareAddressString,
)

factoid = "mac_address"


def fact():
    '''Returns the mac address of this Mac'''
    net_config = SCDynamicStoreCreate(None, "net", None, None)
    states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
    primary_interface = states["PrimaryInterface"]
    primary_device = [
        x
        for x in SCNetworkInterfaceCopyAll()
        if SCNetworkInterfaceGetBSDName(x) == primary_interface
    ][
        0
    ]
    primary_MAC = SCNetworkInterfaceGetHardwareAddressString(primary_device)
    return {factoid: primary_MAC}


if __name__ == "__main__":
    print "<result>%s</result>" % fact()[factoid]
