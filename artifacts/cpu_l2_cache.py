import plistlib
import subprocess

factoid = "cpu_l2_cache"


def fact():
    """Returns the CPU L2 cache"""

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
        result = d[0]["_items"][0].get("l2_cache_core", "")

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
