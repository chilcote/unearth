factoid = "crashplan_username"


def fact():
    """Return CrashPlan user name"""
    cp_identity_file = "/Library/Application Support/CrashPlan/.identity"
    result = ""
    try:
        with open(cp_identity_file) as identity:
            for line in identity.readlines():
                if line.startswith("username="):
                    result = line.partition("=")[2].rstrip()
                    break
    except (IOError, OSError):
        pass

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
