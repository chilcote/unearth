import subprocess
from collections import Counter

factoid = 'most_frequent_user'

def fact():
    '''Return the most frequent user'''
    most_frequent_user = None
    users = []

    output = subprocess.check_output(['/usr/bin/last'] )
    for line in output.splitlines():
        if line: users.append(line.split()[0])
    most_frequent_user = Counter(users).most_common()[0][0]

    return {factoid: most_frequent_user}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
