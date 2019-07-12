import datetime
import subprocess

factoid = "boot_age"


def fact():
    """Returns the number of days since last boot"""

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
        boot_date = datetime.datetime.fromtimestamp(
            int(stdout.strip().split(" = ")[1].split(",")[0])
        ).date()
        today = datetime.datetime.utcnow().date()
        result = (today - boot_date).days

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
