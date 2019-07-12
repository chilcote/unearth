from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "active_directory_trust_account"


def fact():
    """Returns Active Directory trust account"""
    result = "None"

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    d = SCDynamicStoreCopyValue(net_config, "com.apple.opendirectoryd.ActiveDirectory")

    if d:
        result = d.get("TrustAccount", None)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
