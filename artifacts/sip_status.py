import subprocess

factoid = 'sip_status'

def fact():
    '''Return the current SIP status for the startup disk'''
    try:
        proc = subprocess.Popen(['/usr/bin/csrutil', 'status'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = 'Unknown'

    return {factoid: stdout.strip()}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
