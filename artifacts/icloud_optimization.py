import os

from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "icloud_optimization"


def fact():
    """Returns the iCloud disk optimization status"""

    result = "None"

    console_user = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    plist = "/Users/%s/Library/Preferences/com.apple.bird.plist" % console_user

    if os.path.exists(plist):
        result = CFPreferencesCopyAppValue("optimize-storage", plist)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
