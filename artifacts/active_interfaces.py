import subprocess
from SystemConfiguration import (
        SCNetworkInterfaceGetBSDName,
        SCNetworkInterfaceCopyAll,
        SCNetworkInterfaceGetBSDName
        )

factoid = 'active_interfaces'

def fact():
    '''Return the active network interfaces'''
    result = []

    interfaces = [
        SCNetworkInterfaceGetBSDName(i)
        for i in SCNetworkInterfaceCopyAll()
        ]

    for i in interfaces:
        try:
            active = subprocess.check_output(['/usr/sbin/ipconfig', 'getifaddr', i]).strip()
            if active:
                result.append(i)
        except subprocess.CalledProcessError:
            continue

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % ','.join(fact()[factoid])
