import subprocess

from SystemConfiguration import SCDynamicStoreCopyValue, SCDynamicStoreCreate

factoid = "cidr"


def get_iface(net_config):
    """Returns the primary interface of this Mac"""

    iface = None

    try:
        states = SCDynamicStoreCopyValue(net_config, "State:/Network/Global/IPv4")
        iface = states["PrimaryInterface"]
    except TypeError:
        pass

    return iface


def ip_address(iface, net_config, addresses=[]):
    """Returns the IP of this Mac"""

    ip = None

    try:
        addresses = SCDynamicStoreCopyValue(
            net_config, "State:/Network/Interface/%s/IPv4" % iface
        )
    except TypeError:
        pass

    if addresses:
        try:
            ip = addresses["Addresses"][0]
        except TypeError:
            pass

    return ip


def fact():
    """Returns the cidr of the current vlan"""

    result = "None"

    net_config = SCDynamicStoreCreate(None, "net", None, None)
    ip, primary_interface, netmask = "", "", ""

    primary_interface = get_iface(net_config)

    if primary_interface:
        ip = ip_address(primary_interface, net_config)

    if ip:
        try:
            proc = subprocess.Popen(
                ["/sbin/ifconfig", primary_interface],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, _ = proc.communicate()
        except (IOError, OSError):
            stdout = None

        if stdout:
            for line in stdout.splitlines():
                if ip in line.decode():
                    netmask = line.decode().split(" ")[3].lower()
            count = int(0)
            count += int(netmask.count("f")) * 4
            count += int(netmask.count("e")) * 3
            count += int(netmask.count("c")) * 2
            count += int(netmask.count("8")) * 1

            result = "%s.%s/%s" % (".".join(ip.split(".")[0:3]), "0", count)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
