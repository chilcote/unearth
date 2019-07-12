import plistlib
import subprocess

factoid = "smc_version"


def fact():
    """Returns the smc version info"""
    smc_version = None

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/system_profiler", "SPHardwareDataType", "-xml"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
        d = plistlib.readPlistFromString(stdout.strip())
        smc_version = d[0]["_items"][0].get("SMC_version_system", "None")
    except (IOError, OSError):
        pass

    return {factoid: smc_version}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
