import plistlib
import subprocess

factoid = "cpu_cores"


def fact():
    """Returns the number of CPU cores"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/system_profiler", "SPHardwareDataType", "-xml"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = plistlib.loads(stdout.strip())
        result = d[0]["_items"][0]["number_processors"]

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
