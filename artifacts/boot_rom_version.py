import plistlib
import subprocess

factoid = "boot_rom_version"


def fact():
    """Returns the boot rom version"""

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
        result = d[0]["_items"][0]["boot_rom_version"]

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
