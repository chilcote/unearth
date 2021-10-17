"""Return the current machine shard value.

This should match the get_shard function from https://goo.gl/E6M5wR
"""

import hashlib
import plistlib
import subprocess


def get_serial():
    output = subprocess.check_output(
        ["/usr/sbin/ioreg", "-c", "IOPlatformExpertDevice", "-d", "2", "-a"]
    )
    serial = plistlib.loads(output)["IORegistryEntryChildren"][0][
        "IOPlatformSerialNumber"
    ]

    return serial


def fact():
    """Return the machine shard value based off the serial number."""
    serial = get_serial()
    if serial is None:
        return 0
    shard = int(int(hashlib.md5(serial.encode()).hexdigest(), 16) % 100)
    # we don't want to have a zero shard
    return {"shard": shard + 1}


if __name__ == "__main__":
    print(fact())
