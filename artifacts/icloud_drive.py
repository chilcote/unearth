import os

from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "icloud_drive"


def fact():
    """Returns the icloud drive status"""
    result = "None"
    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    plist = "/Users/%s/Library/Preferences/MobileMeAccounts.plist" % console_user
    if os.path.exists(plist):
        d = CFPreferencesCopyAppValue("Accounts", plist)[0]["Services"][2]
        if d:
            result = d.get("Enabled", False)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
