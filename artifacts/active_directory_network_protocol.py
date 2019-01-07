import subprocess
import plistlib

factoid = 'active_directory_network_protocol'

def fact():
    '''Returns the Active Directory folder network protocol'''

    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/sbin/dsconfigad', '-show', '-xml'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = plistlib.readPlistFromString(stdout.strip())
        data = [d]
        result = data[0]['User Experience']['Network protocol']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
