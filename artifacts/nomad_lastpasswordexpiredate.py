from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "nomad_lastpasswordexpiredate"


def fact():
    """Gets the LastPasswordExpireDate value from the nomad plist"""
    result = ""

    username = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    if username:
        result = CFPreferencesCopyAppValue(
            "LastPasswordExpireDate",
            "/Users/%s/Library/Preferences/com.trusourcelabs.NoMAD.plist" % username,
        )

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
