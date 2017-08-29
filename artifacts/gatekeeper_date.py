import datetime
import os
import plistlib
import subprocess
import time
from distutils.version import LooseVersion

factoid = 'gatekeeper_date'

def fact():
    '''Returns the modification date of the gatekeeper package'''
    result = 'None'

    try:
        gkpkgs = subprocess.check_output(['/usr/sbin/pkgutil',
                                        '--pkgs=.*Gatekeeper.*'])
        dates = []
        for pkgid in gkpkgs.splitlines():
            pkginfo_plist = subprocess.check_output(['/usr/sbin/pkgutil',
                                                     '--pkg-info-plist', pkgid])
            pkginfo       = plistlib.readPlistFromString(pkginfo_plist)
            dates.append(pkginfo['install-time'])
        result = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(max(dates)))
    except (OSError, IOError):
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
