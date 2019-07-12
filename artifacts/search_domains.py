from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "search_domains"


def fact():
    """Returns the current search domains"""
    search_domains = None

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    search_domains = []
    dns_info = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/DNS")
    if dns_info and dns_info.get("SearchDomains"):
        try:
            for i in dns_info["SearchDomains"]:
                search_domains.append(i)
        except KeyError:
            pass

    return {factoid: search_domains}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
