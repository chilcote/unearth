from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'primary_interface'

def fact():
    '''Returns the primary interface of this Mac'''
    primary_interface = None
    net_config = SCDynamicStoreCreate(None, "net", None, None)
    try:
        states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
        primary_interface = states['PrimaryInterface']
    except TypeError:
        pass

    return {factoid: primary_interface}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
