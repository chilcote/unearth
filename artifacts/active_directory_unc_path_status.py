import subprocess
import plistlib

factoid = 'active_directory_unc_path_status'

def fact():
    '''Returns the status of Active Directory UNC path'''

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
        result = data[0]['User Experience']['Use Windows UNC path for home']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
