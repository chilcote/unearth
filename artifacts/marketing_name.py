# ref: http://scriptingosx.com/2017/11/get-the-marketing-name-for-a-mac/
import plistlib
import subprocess

from Cocoa import NSBundle

factoid = "marketing_name"


def fact():
    """Returns the marketing name"""
    result = "None"
    model = subprocess.check_output(["/usr/sbin/sysctl", "-n", "hw.model"]).strip()

    serverInfoBundle = NSBundle.bundleWithPath_(
        "/System/Library/PrivateFrameworks/ServerInformation.framework/"
    )
    sysinfofile = serverInfoBundle.URLForResource_withExtension_subdirectory_(
        "SIMachineAttributes", "plist", ""
    )

    d = plistlib.readPlist(sysinfofile.path())

    if d.get(model, False):
        result = d[model]["_LOCALIZABLE_"]["marketingModel"]

    return {factoid: result.strip()}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
