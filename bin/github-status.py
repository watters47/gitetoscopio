#!/usr/bin/env python
#coding: utf-8
"""
Example of accessing the API of status.github.com
You may want to use this example to build a check for Icinga
"""


import sys
from gitetoscopio import GithubStatusAPI


if __name__ == '__main__':
    api = GithubStatusAPI()
    status = api.getStatus()

    desc = status['status']
    if desc == 'good':
        value = 0
    elif desc == 'minor':
        value = 1
    elif desc == 'major':
        value = 2
    else:
        value = 1 # API changed

    message = 'Status: %s, at %s' % (desc, status['last_updated'])
    print message

    sys.exit(value)

