import subprocess
import plistlib

factoid = 'filesystem_type'

def fact():
    '''Returns the filesytem type'''
    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/sbin/diskutil', 'info', '-plist', '/'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = plistlib.readPlistFromString(stdout.strip())
        result = d.get('FilesystemType', 'None')

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
