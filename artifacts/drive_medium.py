import subprocess
import plistlib

factoid = "drive_medium"

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
        if 'Fusion' in stdout:
            result = 'fusion'
        else:
            # Determine rotational vs ssd
            proc = subprocess.Popen(['/usr/sbin/system_profiler', '-xml',
                                        'SPStorageDataType'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            stdout, _ = proc.communicate()
            xml = plistlib.readPlistFromString(stdout)
            drives = xml[0]['_items']
            for drive in drives:
                if drive['mount_point'] == '/':
                    # Check for CoreStorage physical volume
                    try:
                        result = drive[0]['com.apple.corestorage.pv']['medium_type']
                    except KeyError:
                        result = drive['physical_drive']['medium_type']
    except (IOError, OSError):
        pass
    
    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]