from CoreFoundation import CFPreferencesCopyAppValue

factoid = "updates_software_days_delay"


def fact():
    """Returns the status of automatic downloading of software updates"""
    status = "disabled"
    pref = CFPreferencesCopyAppValue(
        "enforcedSoftwareUpdateDelay", "/Library/Preferences/com.apple.SoftwareUpdate"
    )
    if pref:
        status = pref

    return {factoid: status}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
