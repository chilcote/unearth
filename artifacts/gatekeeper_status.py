import subprocess

factoid = 'gatekeeper_status'

def fact():
    '''Return the current Gatekeeper status'''
    result = 'None'

    try:
        proc = subprocess.Popen(['/usr/sbin/spctl', '--status'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, _ = proc.communicate()
    except (IOError, OSError):
        result = 'Unknown'

    return {factoid: result.strip()}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
