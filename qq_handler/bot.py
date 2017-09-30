#!/usr/bin/env python
# coding: utf-8

from smartqq.utils import *
from config import Constant

import time
import grequests


class Bot(object):

    def __init__(self):
        self.bot_list = [
            'tuling-bot',
            'test-bot',
        ]
        self.active_bot = self.bot_list[1]

    def get_many_reply(self, need_reply_list):
        def except_handler(r, e):
            echo('request bot reply failed\n')
            return None

        if self.active_bot == self.bot_list[0]:
            api_key = Constant.BOT_TULING_API_KEY
            api_urls = [Constant.BOT_TULING_API_URL % (api_key, ne_reply['text'], ne_reply['user'])
                        for ne_reply in need_reply_list]
            result = []
            for i in xrange(0, len(api_urls), 100):
                reqs = [grequests.get(url) for url in api_urls[i:i + 100]]
                responses = grequests.map(reqs, exception_handler=except_handler)
                rs = map(lambda r: json.loads(r.content) if r else None, responses)
                for rg in rs:
                    if rg:
                        if rg.get('code') == 100000 and rg.get('text'):
                            result.append(trans_coding(rg['text']))
                        else:
                            result.append(Constant.BOT_TULING_BOT_REPLY)
                    else:
                        result.append(Constant.BOT_TULING_BOT_REPLY)

        elif self.active_bot == self.bot_list[1]:
            api_url = 'http://192.168.100.202:9060'
            api_data = [
                json.dumps({
                    'query': ne_reply['text'],
                })
                for ne_reply in need_reply_list
            ]
            result = []
            for k in xrange(0, len(need_reply_list), 100):
                reqs = [grequests.post(url=api_url, data=data) for data in api_data[k:k + 100]]
                responses = grequests.map(reqs, exception_handler=except_handler)
                rs = map(lambda r: json.loads(r.content) if r else None, responses)
                for rg in rs:
                    if rg:
                        result.append(trans_coding(rg['answer']))
                    else:
                        result.append('None')
        else:
            result = []
        return result
