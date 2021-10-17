import plistlib
import subprocess

factoid = "profiles_count"


def fact():
    """Returns the count of system profiles"""
    profiles = None

    cmd = ["/usr/bin/profiles", "-Co", "stdout-xml"]
    task = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = task.stdout.read()

    if out:
        d = plistlib.loads(out)
        if d:
            profiles = len(d["_computerlevel"])

    return {factoid: profiles}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
