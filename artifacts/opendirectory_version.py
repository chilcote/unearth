import subprocess

factoid = 'opendirectoryd_version'

def fact():
    '''
    Returns the "project version" number used to build opendirectoryd
    per https://support.apple.com/en-gb/HT208315 to check that
    "Security Update 2017-001" is installed
    '''

    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/bin/what', '/usr/libexec/opendirectoryd'],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        result = stdout.splitlines()[-1].split(':')[-1]

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]