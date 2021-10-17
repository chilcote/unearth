import plistlib
import subprocess

factoid = "profiles_system"


def fact():
    """Returns the system profiles"""
    profiles = []

    cmd = ["/usr/bin/profiles", "-Co", "stdout-xml"]
    task = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = task.stdout.read()

    if out:
        d = plistlib.loads(out)
        if d:
            for i in d["_computerlevel"]:
                profiles.append(i["ProfileDisplayName"])

    return {factoid: profiles}


if __name__ == "__main__":
    print("<result>%s</result>" % ",".join(fact()[factoid]))
