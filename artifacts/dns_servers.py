from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "dns_servers"


def fact():
    """Returns the current dns servers"""
    result = []

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    dns_info = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/DNS")
    if dns_info and dns_info.get("ServerAddresses"):
        try:
            for i in dns_info["ServerAddresses"]:
                result.append(i)
        except KeyError:
            pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % ",".join(fact()[factoid]))
