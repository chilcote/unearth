import subprocess

factoid = "file_sharing_status_smb"


def fact():
    """Returns the status of SMB file sharing"""
    try:
        status = False
        proc = subprocess.Popen(
            ["/bin/launchctl", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        result, _ = proc.communicate()
        if "com.apple.smbd" in result:
            status = True
    except (IOError, OSError):
        status = "Unknown"

    return {factoid: status}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
