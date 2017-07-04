import objc

factoid = 'wifi_status'

def fact():
    '''Returns the wifi power status of the Mac'''
    wifi_status = None
    objc.loadBundle('CoreWLAN',
                    bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals=globals())

    wifi = CWInterface.interfaceNames()
    if wifi:
        for iname in wifi:
            interface = CWInterface.interfaceWithName_(iname)
        try:
            wifi_status = "On" if interface.powerOn() == 1 else "Off"
        except AttributeError:
            wifi_status = None
    return {factoid: wifi_status}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
