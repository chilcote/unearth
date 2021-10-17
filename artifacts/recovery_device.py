import plistlib
import subprocess

factoid = "recovery_device"


def fact():
    """Returns the boot volume of this Mac"""
    try:
        proc = subprocess.Popen(
            ["/usr/sbin/diskutil", "info", "-plist", "/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        d = plistlib.loads(stdout.strip())
        recovery_device = d["RecoveryDeviceIdentifier"]
    except (IOError, OSError):
        pass

    return {factoid: recovery_device}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
