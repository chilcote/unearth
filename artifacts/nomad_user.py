from CoreFoundation import CFPreferencesCopyAppValue
from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "nomad_user"


def fact():
    """Gets the assigned user from the nomad plist"""
    result = ""

    username = SCDynamicStoreCopyConsoleUser(None, None, None)[0]
    if username:
        result = CFPreferencesCopyAppValue(
            "UserShortName",
            "/Users/%s/Library/Preferences/com.trusourcelabs.NoMAD.plist" % username,
        )

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
