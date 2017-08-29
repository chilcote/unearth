import urllib2

factoid = 'external_ip'

def fact():
    '''Returns the external IP of this Mac'''
    result = 'None'

    url = 'http://ipecho.net/plain'
    url = 'http://icanhazip.com'
    try:
        data = urllib2.urlopen(url).read()
        result = data.strip()
    except urllib2.URLError as err:
        result = 'Unknown'
    except:
        pass

    return {factoid: result}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
