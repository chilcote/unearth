import subprocess

factoid = 'opendirectoryd_build_number'

def fact():
    '''
    Returns the "project version" number used to build opendirectoryd
    per https://support.apple.com/en-gb/HT208315 to check that
    "Security Update 2017-001" is installed
    '''

    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/libexec/opendirectoryd', '-v'],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        result = stdout.split('(', 1)[1].split(')')[0].split(' ')[-1]

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]