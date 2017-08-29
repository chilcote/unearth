import os, subprocess

factoid = 'sentinel_server'

def fact():
    '''Returns the sentinel server'''
    server = 'None'
    binary = '/usr/local/bin/sentinelctl'
    if os.path.exists(binary) and os.getuid() == 0:
        try:
            output = subprocess.check_output([binary, 'online'])
            for line in output.splitlines():
                if 'server' in line:
                    server = line.split()[-1]
        except:
            pass

    return {factoid: server}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
