import subprocess
import plistlib

factoid = 'drive_medium'

def fact():
    '''
    Returns the medium type for the boot drive of this Mac

    Values include 'fusion', 'rotational', 'ssd' or 'None'
    '''
    result = 'None'
    try:
        # Check for Fusion drive
        proc = subprocess.Popen(['/usr/sbin/diskutil', 'cs', 'list'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
        if 'fusion' in stdout.lower():
            result = 'fusion'
        else:
            # Determine rotational vs ssd
            proc = subprocess.Popen(['/usr/sbin/system_profiler', '-xml',
                                     'SPStorageDataType'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            stdout, _ = proc.communicate()
            drives = plistlib.readPlistFromString(stdout)[0]['_items']
            for drive in drives:
                if drive['mount_point'] == '/':
                    # Check for CoreStorage physical volume
                    try:
                        result = drive['com.apple.corestorage.pv'][0]['medium_type']
                    except KeyError:
                        result = drive['physical_drive']['medium_type']
                    except KeyError:
                        pass
    except (IOError, OSError):
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
