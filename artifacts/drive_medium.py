import subprocess
import plistlib

factoid = 'drive_medium'

def fact():
    '''Returns the boot drive medium'''
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
        if d.get('CoreStorageCompositeDisk', False):
            result = 'fusion'
        elif d.get('RAIDMaster', False):
            result = 'raid'
        else:
            result = 'ssd' if d.get('SolidState', False) else 'rotational'

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
