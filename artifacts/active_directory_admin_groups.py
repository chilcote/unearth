import plistlib
import subprocess

factoid = "active_directory_admin_groups"


def fact():
    """Returns the Active Directory groups with administrative privileges"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/dsconfigad", "-show", "-xml"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = plistlib.readPlistFromString(stdout.strip())
        data = [d]
        result = data[0]["Administrative"]["Allowed admin groups"]

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
