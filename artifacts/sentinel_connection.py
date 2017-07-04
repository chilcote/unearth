import os, subprocess

factoid = 'sentinel_connection'

def fact():
    '''Returns the sentinel connection'''
    last_seen = None
    binary = '/usr/local/bin/sentinelctl'
    if os.path.exists(binary) and os.getuid() == 0:
        try:
            output = subprocess.check_output([binary, 'online'])
            for line in output.splitlines():
                if 'last seen' in line:
                    last_seen = line.split()[-1]
        except:
            pass

    return {factoid: last_seen}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
