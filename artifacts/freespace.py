import plistlib
import subprocess

factoid = "freespace"


def fact():
    """Returns the free space of the boot drive of this Mac"""
    result = "None"
    try:
        proc = subprocess.Popen(
            ["/usr/sbin/diskutil", "info", "-plist", "/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        xml = plistlib.readPlistFromString(stdout)
        result = int(xml["FreeSpace"]) / 1000 / 1000 / 1000
    except (IOError, OSError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
