import subprocess

factoid = "filevault_status"


def fact():
    """Return the current FileVault status for the startup disk"""
    try:
        proc = subprocess.Popen(
            ["/usr/bin/fdesetup", "status"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        result, _ = proc.communicate()
    except (IOError, OSError):
        result = "Unknown"

    return {factoid: result.strip()}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
