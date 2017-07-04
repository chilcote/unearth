import subprocess
import plistlib

factoid = 'memory'

def fact():
    '''Returns the memory in GBs'''
    memory = None
    try:
        proc = subprocess.Popen(['/usr/sbin/sysctl', '-n', 'hw.memsize'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
        memory = int(stdout.strip())/1024/1024/1024
    except (IOError, OSError):
        pass

    return {factoid: memory}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
