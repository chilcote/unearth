from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = 'directory_contacts_node'

def fact():
    '''Returns the directory search node info'''
    result = 'None'
    net_config = SCDynamicStoreCreate(None, "net", None, None)

    contacts_node = SCDynamicStoreCopyValue(
            net_config,
           "com.apple.opendirectoryd.node:/Contacts"
           )
    if contacts_node:
        result = contacts_node[0]

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
