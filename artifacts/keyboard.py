# ref: allister in slack
import plistlib
import subprocess

factoid = "keyboard"


def fact():
    """Returns the keyboard localization"""
    result = ""

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/ioreg", "-rln", "AppleHIDKeyboardEventDriverV2", "-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output, _ = proc.communicate()
    except (IOError, OSError):
        result = "Unknown"

    if output:
        result = plistlib.readPlistFromString(output)[0].get("KeyboardLanguage")

    return {factoid: result.strip()}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
