import os

from CoreFoundation import CFPreferencesCopyAppValue

factoid = "active_directory_dsbindtimeout"


def fact():
    """Returns the dsbindtimeout setting"""

    result = "None"
    plist = "/Library/Preferences/com.apple.loginwindow.plist"

    if plist and os.path.exists(plist):
        result = CFPreferencesCopyAppValue("DSBindTimeout", plist)

    return {factoid: str(result)}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
