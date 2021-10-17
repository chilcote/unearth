import plistlib
import subprocess

from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "console_user_is_admin"


def fact():
    """Returns whether current console user is an admin"""
    result = False

    cmd = ["/usr/bin/dscl", "-plist", ".", "read", "/Groups/admin"]
    output = subprocess.check_output(cmd)
    d = plistlib.loads(output)["dsAttrTypeStandard:GroupMembership"]

    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    if console_user in d:
        result = True

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
