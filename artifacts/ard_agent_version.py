import subprocess

factoid = 'ard_agent_version'

def fact():
    '''Returns the Apple Remote Desktop agent version'''

    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/bin/defaults', 'read', '/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/version.plist', 'CFBundleShortVersionString'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        result = stdout.strip()

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
