from CoreFoundation import CFPreferencesCopyAppValue

factoid = "updates_config_data"


def fact():
    """Returns the status of automatic installation of config data"""
    status = "disabled"
    pref = CFPreferencesCopyAppValue(
        "ConfigDataInstall", "/Library/Preferences/com.apple.SoftwareUpdate"
    )
    if pref:
        status = "enabled"

    return {factoid: status}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
