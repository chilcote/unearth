import subprocess

factoid = "bootcamp_status"


def fact():
    """Returns bootcamp status"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/diskutil", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        for line in stdout.strip().splitlines():
            result = True if b"Microsoft Basic Data" in line else False

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
