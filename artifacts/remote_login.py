import os
import subprocess

factoid = "remote_login"


def fact():
    """Returns whether remote login is activated"""
    remote_login = None
    if os.geteuid() == 0:
        output = subprocess.check_output(["/usr/sbin/systemsetup", "getremotelogin"])
        remote_login = output.split(": ")[1].strip()
    else:
        remote_login = "Unknown"

    return {factoid: remote_login}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
