from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'computername'

def fact():
    '''Returns the ComputerName'''
    result = None

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    sys_info = SCDynamicStoreCopyValue(net_config, "Setup:/System")
    result = sys_info['ComputerName']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
