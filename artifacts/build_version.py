import subprocess

factoid = "build_version"


def fact():
    """Returns the macOS build version"""
    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/sysctl", "-n", "kern.osversion"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        result = stdout.strip()

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
