import subprocess

factoid = 'opendirectoryd_build_number'

def fact():
    '''
    Returns the current build number of opendirectoryd
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