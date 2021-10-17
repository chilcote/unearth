from CoreFoundation import CFPreferencesCopyAppValue

factoid = "updates_software_delay"


def fact():
    """Returns the status of delay of software updates"""
    status = "disabled"
    pref = CFPreferencesCopyAppValue(
        "forceDelayedSoftwareUpdates", "/Library/Preferences/com.apple.SoftwareUpdate"
    )
    if pref:
        status = "enabled"

    return {factoid: status}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
