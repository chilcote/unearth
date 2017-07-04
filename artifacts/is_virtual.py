import subprocess

factoid = 'is_virtual'

def fact():
    '''Returns whether the system is a virtual machine'''
    result = None
    try:
        proc = subprocess.Popen(['/usr/sbin/sysctl', '-n', 'machdep.cpu.features'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
        result = True if 'VMM' in stdout else False
    except (IOError, OSError):
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
