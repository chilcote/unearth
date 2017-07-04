import subprocess

factoid = 'hardware_model'

def fact():
    '''Returns the hardware model'''
    result = None

    try:
        proc = subprocess.Popen(['/usr/sbin/sysctl', '-n', 'hw.model'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, _ = proc.communicate()
    except (IOError, OSError):
        result = 'Unknown'

    return {factoid: result.strip()}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
