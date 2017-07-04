import subprocess
import plistlib

factoid = 'boot_volume'

def fact():
    '''Returns the boot volume'''
    result = None

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
        result = d['VolumeName']

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
