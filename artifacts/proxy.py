from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "proxies"


def fact():
    """Returns the current dns servers"""
    proxies = "None"

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    proxy_info = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/Proxies")
    if proxy_info and proxy_info.get("ProxyAutoConfigURLString"):
        try:
            proxies = proxy_info["ProxyAutoConfigURLString"]
        except KeyError:
            pass

    return {factoid: proxies}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
