import datetime
import subprocess

factoid = "boot_date"


def fact():
    """Returns the system boot time"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["sysctl", "-n", "kern.boottime"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        result = datetime.datetime.fromtimestamp(
            int(stdout.strip().split(" = ")[1].split(",")[0])
        ).strftime("%Y-%m-%dT%H:%M:%S")

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
