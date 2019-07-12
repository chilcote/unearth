import os
import subprocess

factoid = "firmware_password_status"


def fact():
    """Returns whether or not a firmware password is set"""

    result = "None"

    if os.geteuid() == 0:
        try:
            proc = subprocess.Popen(
                ["/usr/sbin/firmwarepasswd", "-check"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, _ = proc.communicate()
        except (IOError, OSError):
            stdout = None

        if stdout:
            result = True if stdout.split()[-1] == "Yes" else False
    else:
        result = "Unknown"

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
