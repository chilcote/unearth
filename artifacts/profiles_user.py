import os
import plistlib
import subprocess

from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "profiles_user"


def fact():
    """Returns the user profiles"""
    profiles = []
    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]

    if os.getuid() == 0:
        cmd = ["sudo", "-u", console_user, "/usr/bin/profiles", "-Lo", "stdout-xml"]
    else:
        cmd = ["/usr/bin/profiles", "-Lo", "stdout-xml"]
    task = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = task.stdout.read()

    if out:
        d = plistlib.readPlistFromString(out)
        if d:
            for i in d[console_user]:
                profiles.append(i["ProfileDisplayName"])

    return {factoid: profiles}


if __name__ == "__main__":
    print("<result>%s</result>" % ",".join(fact()[factoid]))
