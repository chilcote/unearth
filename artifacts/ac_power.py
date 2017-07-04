import subprocess

factoid = 'ac_power'

def fact():
    '''Returns whether drawing from AC Power source'''

    result = False

    try:
        proc = subprocess.Popen(
                ['/usr/bin/pmset', '-g', 'ps'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
        for line in stdout.splitlines():
            if 'AC Power' in line:
                result = True
    except (IOError, OSError):
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
