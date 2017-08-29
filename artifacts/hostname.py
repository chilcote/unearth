from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'hostname'

def fact():
    '''Returns the value of the hostname of this Mac'''
    result = 'None'

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    sys_info = SCDynamicStoreCopyValue(net_config, "Setup:/System")
    result = sys_info['HostName']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
