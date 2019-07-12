import os

from CoreFoundation import CFPreferencesCopyAppValue

factoid = "java_plugin_version"


def fact():
    """Returns the java plugin version"""
    result = "None"

    plist = "/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Info.plist"
    if os.path.exists(plist):
        result = CFPreferencesCopyAppValue("CFBundleVersion", plist)

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
