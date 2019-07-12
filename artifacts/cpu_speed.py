import plistlib
import subprocess

factoid = "cpu_speed"


def fact():
    """Returns the CPU frequency"""

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
        d = plistlib.readPlistFromString(stdout.strip())
        result = d[0]["_items"][0]["current_processor_speed"]

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
