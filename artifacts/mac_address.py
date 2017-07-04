import imp
import os
import subprocess
import sys
from SystemConfiguration import SCDynamicStoreCreate, SCDynamicStoreCopyValue

factoid = 'mac_address'

def get_external_fact(category):
    '''Returns info from another module in this project'''
    d = {}
    filename = os.path.join(os.path.dirname(__file__), category + '.py')
    if os.path.exists(filename):
        try:
            module = imp.load_source(category, filename)
            d = module.fact()
        except (ImportError, AttributeError), err:
            print >> sys.stderr, 'Error %s in file %s' % (err, filename)
    return d[category]

def fact():
    '''Returns the mac address of this Mac'''
    mac_address = None
    primary_interface = get_external_fact('primary_interface')
    if primary_interface:
        try:
            proc = subprocess.Popen(['/usr/sbin/networksetup',
                                    '-getmacaddress',
                                    primary_interface],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = proc.communicate()
            mac_address = stdout.strip().split(' ')[2]
        except (IOError, OSError):
            pass

    return {factoid: mac_address}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
