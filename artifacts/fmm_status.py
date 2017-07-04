import subprocess, plistlib

factoid = 'fmm_status'

def fact():
    '''Return the Find My Mac status'''
    result = False
    try:
        proc = subprocess.Popen(['/usr/sbin/nvram', '-x', '-p', 'status'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = ''

    if stdout:
        if plistlib.readPlistFromString(stdout).get('fmm-mobileme-token-FMM', None):
            result = True
        return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
