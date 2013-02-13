#!/usr/bin/env python
#coding: utf-8

import json
import iso8601
from urllib2 import urlopen


def http_get_query(url):
    answer_f = urlopen(url)
    answer_json = answer_f.read()
    answer = json.loads(answer_json)
    return answer


def str2dt(text):
    return iso8601.parse_date(text)


def convert_date(d, key):
    d[key] = str2dt(d[key])


class GithubStatusAPI():
    def __init__(self, refresh_urls=True):
        self.status = None
        self.messages = None
        self.last_message = None

        self.methods_url = 'https://status.github.com/api.json'

        if refresh_urls:
            pointers = http_get_query(self.methods_url)
            self.status_url = pointers['status_url']
            self.messages_url = pointers['messages_url']
            self.last_message_url = pointers['last_message_url']
        else:
            self.status_url = 'https://status.github.com/api/status.json'
            self.messages_url = 'https://status.github.com/api/messages.json'
            self.last_message_url = 'https://status.github.com/api/last-message.json'

    def getStatus(self):
        self.status = http_get_query(self.status_url)
        convert_date(self.status, 'last_updated')
        return self.status

    def getMessages(self):
        self.messages = http_get_query(self.messages_url)
        for msg in self.messages:
            convert_date(msg, 'created_on')
        return self.messages

    def getLastMessage(self):
        self.last_message = http_get_query(self.last_message_url)
        convert_date(self.last_message, 'created_on')
        return self.last_message


# FIXME: remove this
if __name__ == '__main__':
    api = GithubStatusAPI()
    st = api.getStatus()
    print st['status']
    print st['last_updated']
    print ''

    st = api.getLastMessage()
    print st['status']
    print st['body']
    print st['created_on']
    print ''

    st = api.getMessages()
    print len(st)
    for m in st:
        print m

