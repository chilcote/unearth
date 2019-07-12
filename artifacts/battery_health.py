import plistlib
import subprocess

factoid = "battery_health"


def fact():
    """Returns the battery health"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/ioreg", "-r", "-c", "AppleSmartBattery", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        if stdout:
            d = plistlib.readPlistFromString(stdout)[0]
            result = "Healthy" if not d["PermanentFailureStatus"] else "Failing"
    except (IOError, OSError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
