from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "active_directory_node"


def fact():
    """Returns Active Directory node"""
    result = "None"

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    d = SCDynamicStoreCopyValue(net_config, "com.apple.opendirectoryd.ActiveDirectory")

    if d:
        result = d.get("NodeName", None)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
