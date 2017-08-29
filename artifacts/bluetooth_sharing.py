# ref: bruienne in slack
import objc

factoid = 'bluetooth_sharing'

def fact():
    '''Returns the current bluetooth sharing'''

    result = 'None'

    objc.loadBundle("IOBluetooth", globals(), bundle_path=objc.pathForFramework(u'/System/Library/Frameworks/IOBluetooth.framework'))
    btprefs = IOBluetoothPreferences.alloc().init()
    result = bool(btprefs.fileTransferServicesEnabled())

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
