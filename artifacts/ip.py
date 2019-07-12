from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "ip"


def primary_interface():
    """Returns the primary interface of this Mac"""
    primary_interface = None
    net_config = SCDynamicStoreCreate(None, "net", None, None)
    try:
        states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
        primary_interface = states["PrimaryInterface"]
    except TypeError:
        pass

    return primary_interface


def fact():
    """Returns the IP of this Mac"""
    ip = None

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    iface = primary_interface()
    addresses = SCDynamicStoreCopyValue(
        net_config, "State:/Network/Interface/%s/IPv4" % iface
    )

    if addresses:
        try:
            ip = addresses["Addresses"][0]
        except TypeError:
            ip = None

    return {factoid: ip}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
