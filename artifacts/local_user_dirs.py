import os

factoid = 'local_user_dirs'

def fact():
    '''Return the list of user home directories under /Users'''
    # skip_names should include any directories you wish to ignore
    skip_names = ['Shared', 'admin']
    user_dirs = [item for item in os.listdir('/Users')
                 if item not in skip_names and not item.startswith('.')]
    return {factoid: user_dirs}

if __name__ == '__main__':
    print '<result>%s</result>' % fact()[factoid]
