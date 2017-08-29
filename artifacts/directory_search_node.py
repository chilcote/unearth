from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = 'directory_search_node'

def fact():
    '''Returns the directory search node info'''
    result = 'None'
    net_config = SCDynamicStoreCreate(None, "net", None, None)

    search_node = SCDynamicStoreCopyValue(net_config,
                                          "com.apple.opendirectoryd.node:/Contacts")
    result = search_node[0]

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
