import plistlib
import subprocess

factoid = "serial_number"


def fact():
    """Returns the serial number of this Mac."""
    output = subprocess.check_output(
        ["/usr/sbin/ioreg", "-c", "IOPlatformExpertDevice", "-d", "2", "-a"]
    )
    serial = plistlib.loads(output)["IORegistryEntryChildren"][0][
        "IOPlatformSerialNumber"
    ]

    return {factoid: serial}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
