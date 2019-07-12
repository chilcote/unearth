import objc

factoid = "wifi_ssid"


def fact():
    """Returns the wifi ssid of the Mac"""
    wifi_ssid = None

    objc.loadBundle(
        "CoreWLAN",
        bundle_path="/System/Library/Frameworks/CoreWLAN.framework",
        module_globals=globals(),
    )

    wifi = CWInterface.interfaceNames()
    if wifi:
        for iname in wifi:
            interface = CWInterface.interfaceWithName_(iname)
        if interface:
            try:
                wifi_ssid = interface.ssid()
            except AttributeError:
                pass

    return {factoid: wifi_ssid}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
