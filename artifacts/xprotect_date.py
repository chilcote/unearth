import plistlib
import subprocess
import time

factoid = "xprotect_date"


def fact():
    """Returns the last date xprotect was updated"""

    result = "None"

    try:
        cmd = ["/usr/sbin/pkgutil", "--pkgs=.*XProtect.*"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (pkgs, stderr) = proc.communicate()

        if pkgs:
            dates = []
            for pkgid in pkgs.splitlines():
                pkginfo_plist = subprocess.check_output(
                    ["/usr/sbin/pkgutil", "--pkg-info-plist", pkgid]
                )
                pkginfo = plistlib.loads(pkginfo_plist)
                dates.append(pkginfo["install-time"])

            result = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(max(dates)))
    except (OSError, IOError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
