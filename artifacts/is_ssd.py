import plistlib
import subprocess

factoid = "is_ssd"


def fact():
    """Returns whether the boot drive is an ssd"""
    result = "Unknown"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/diskutil", "info", "-plist", "/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = plistlib.readPlistFromString(stdout.strip())
        if not d.get("CoreStorageCompositeDisk", False) and not d.get(
            "RAIDMaster", False
        ):
            result = d.get("SolidState", False)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
