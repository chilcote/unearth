import plistlib
import re
import subprocess

factoid = 'battery_percentage'

def fact():
    '''Returns the battery percentage'''

    result = 'None'

    try:
        proc = subprocess.Popen(
                ['/usr/bin/pmset', '-g', 'batt'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
                )
        stdout, _ = proc.communicate()
        if stdout:
            if 'InternalBattery' in stdout:
                result = re.findall(r'\d+%', stdout.splitlines()[1])[0].replace('%','')
    except (IOError, OSError):
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
