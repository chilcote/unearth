from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'vpn_active'

def fact():
    '''Check to see if GlobalProtect VPN is active.'''
    result = False

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    vpn = SCDynamicStoreCopyValue(net_config, 'State:/Network/Service/gpd.pan/DNS')
    if vpn is not None:
        result = True

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
