import plistlib
import subprocess

factoid = "battery_status"


def fact():
    """Returns the battery charging status"""

    result = "None"
    charged, charging = None, None

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/ioreg", "-r", "-c", "AppleSmartBattery", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        if stdout:
            charging = plistlib.loads(stdout)[0]["IsCharging"]
            charged = plistlib.loads(stdout)[0]["FullyCharged"]
            if charged and not charging:
                result = "Charged"
            elif charging and not charged:
                result = "Charging"
            elif not charging and not charged:
                result = "Not Charging"
    except (IOError, OSError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
