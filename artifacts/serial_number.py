import objc
from Foundation import NSBundle

factoid = "serial_number"


def fact():
    """Returns the serial number of this Mac."""
    IOKit_bundle = NSBundle.bundleWithIdentifier_("com.apple.framework.IOKit")

    functions = [
        ("IOServiceGetMatchingService", b"II@"),
        ("IOServiceMatching", b"@*"),
        ("IORegistryEntryCreateCFProperty", b"@I@@I"),
    ]
    objc.loadBundleFunctions(IOKit_bundle, globals(), functions)

    kIOMasterPortDefault = 0
    kIOPlatformSerialNumberKey = "IOPlatformSerialNumber"
    kCFAllocatorDefault = None

    platformExpert = IOServiceGetMatchingService(
        kIOMasterPortDefault, IOServiceMatching("IOPlatformExpertDevice")
    )
    serial = IORegistryEntryCreateCFProperty(
        platformExpert, kIOPlatformSerialNumberKey, kCFAllocatorDefault, 0
    )

    return {factoid: serial}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
