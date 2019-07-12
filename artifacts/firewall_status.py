from Foundation import CFPreferencesCopyAppValue

factoid = "firewall_status"


def fact():
    """Returns the firewall status"""
    result = "None"

    plist = "/Library/Preferences/com.apple.alf.plist"
    firewall_status = CFPreferencesCopyAppValue("globalstate", plist)
    result = bool(firewall_status)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
