from CoreFoundation import CFPreferencesCopyAppValue

factoid = "updates_critical"


def fact():
    """Returns the status of automatic installation of critical updates"""
    status = "disabled"
    pref = CFPreferencesCopyAppValue(
        "CriticalUpdateInstall", "/Library/Preferences/com.apple.SoftwareUpdate"
    )
    if pref:
        status = "enabled"

    return {factoid: status}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
