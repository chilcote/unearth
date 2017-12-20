'''Return the current machine shard value.

This should match the get_shard function from https://goo.gl/E6M5wR
'''

import hashlib
import objc
from Foundation import NSBundle


def get_serial():
    '''Return the machine serial number.'''
    IOKit_bundle = NSBundle.bundleWithIdentifier_("com.apple.framework.IOKit")

    functions = [
        ("IOServiceGetMatchingService", b"II@"),
        ("IOServiceMatching", b"@*"),
        ("IORegistryEntryCreateCFProperty", b"@I@@I")
        ]
    objc.loadBundleFunctions(IOKit_bundle, globals(), functions)

    kIOMasterPortDefault = 0
    kIOPlatformSerialNumberKey = 'IOPlatformSerialNumber'
    kCFAllocatorDefault = None

    platformExpert = IOServiceGetMatchingService(
                        kIOMasterPortDefault,
                        IOServiceMatching("IOPlatformExpertDevice")
                     )
    serial = IORegistryEntryCreateCFProperty(platformExpert,
                                             kIOPlatformSerialNumberKey,
                                             kCFAllocatorDefault, 0)

    return serial


def fact():
    '''Return the machine shard value based off the serial number.'''
    serial = get_serial()
    if serial is None:
        return 0
    shard = int(int(hashlib.md5(serial).hexdigest(), 16) % 100)
    # we don't want to have a zero shard
    return {'shard': shard + 1}


if __name__ == '__main__':
    print fact()
