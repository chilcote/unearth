from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'dns_domain'

def fact():
    '''Returns the current dns domain'''
    result = None

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    dns_info = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/DNS")
    if dns_info:
        try:
            result = dns_info.get('DomainName', None)
        except KeyError:
            pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
