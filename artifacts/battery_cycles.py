import plistlib
import subprocess

factoid = "battery_cycles"


def fact():
    """Returns the battery cycle count"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/ioreg", "-r", "-c", "AppleSmartBattery", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        if stdout:
            result = plistlib.readPlistFromString(stdout)[0]["CycleCount"]
    except (IOError, OSError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
