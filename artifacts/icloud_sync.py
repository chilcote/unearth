import glob
import os

from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "icloud_sync"


def fact():
    """Returns the icloud desktop sync status"""

    result = False

    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    plist = "/Users/%s/Library/Preferences/MobileMeAccounts.plist" % console_user
    if os.path.exists(plist):
        d = CFPreferencesCopyAppValue("Accounts", plist)[0]["Services"][2]
        sync_active = d.get("Enabled", False)
        files = glob.glob(
            "/Users/%s/Library/Mobile Documents/com~apple~CloudDocs/*" % console_user
        )
        if sync_active and files:
            for f in files:
                if os.path.islink(f):
                    result = True
                    break

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
