from SystemConfiguration import SCDynamicStoreCopyConsoleUser

factoid = "console_user"


def fact():
    """Returns the current console user"""
    result = SCDynamicStoreCopyConsoleUser(None, None, None)[0]

    return {factoid: result}


if __name__ == "__main__":
    print("<result>%s</result>" % fact()[factoid])
