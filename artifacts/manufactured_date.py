#ref: https://github.com/pudquick/pyMacWarranty
import datetime
import imp
import os
import subprocess
import sys
import time
import objc
from Foundation import NSBundle

factoid = 'manufactured_date'

def get_serial():
    '''Returns the serial number of this Mac.'''
    IOKit_bundle = NSBundle.bundleWithIdentifier_("com.apple.framework.IOKit")

    functions = [
        ("IOServiceGetMatchingService", b"II@"),
        ("IOServiceMatching", b"@*"),
        ("IORegistryEntryCreateCFProperty", b"@I@@I")
        ]
    objc.loadBundleFunctions(IOKit_bundle, globals(), functions)

    kIOMasterPortDefault = 0
    kIOPlatformSerialNumberKey = 'IOPlatformSerialNumber'
    kCFAllocatorDefault = None

    platformExpert = IOServiceGetMatchingService(kIOMasterPortDefault, IOServiceMatching("IOPlatformExpertDevice"))
    serial = IORegistryEntryCreateCFProperty(platformExpert, kIOPlatformSerialNumberKey, kCFAllocatorDefault, 0)

    return serial

def apple_year_offset(dateobj, years=0):
    # Convert to a maleable format
    mod_time = dateobj.timetuple()
    # Offset year by number of years
    mod_time = time.struct_time(tuple([mod_time[0]+years]) + mod_time[1:])
    # Convert back to a datetime obj
    return datetime.datetime.fromtimestamp(int(time.mktime(mod_time)))

def manufacture_date(serial):
    # http://www.macrumors.com/2010/04/16/apple-tweaks-serial-number-format-with-new-macbook-pro/
    est_date = u''
    if 10 < len(serial) < 13:
        if len(serial) == 11:
            # Old format
            year = serial[2].lower()
            est_year = 2000 + '   3456789012'.index(year)
            week = int(serial[3:5]) - 1
            year_time = datetime.date(year=est_year, month=1, day=1)
            if (week):
                week_dif = datetime.timedelta(weeks=week)
                year_time += week_dif
        else:
            # New format
            alpha_year = 'cdfghjklmnpqrstvwxyz'
            year = serial[3].lower()
            est_year = 2010 + (alpha_year.index(year) / 2)
            # 1st or 2nd half of the year
            est_half = alpha_year.index(year) % 2
            week = serial[4].lower()
            alpha_week = ' 123456789cdfghjklmnpqrtvwxy'
            est_week = alpha_week.index(week) + (est_half * 26) - 1
            year_time = datetime.date(year=est_year, month=1, day=1)
            if (est_week):
                week_dif = datetime.timedelta(weeks=est_week)
                year_time += week_dif
    return apple_year_offset(year_time).strftime('%Y-%m-%d')

def fact():
    '''Returns the estimated manufacture date'''
    manufactured_date = None
    serial = get_serial()
    if not serial.startswith('VM'):
        manufactured_date = manufacture_date(serial)

    return {factoid: manufactured_date}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
