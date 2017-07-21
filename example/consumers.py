# -*- coding: UTF-8 -*-
from channels import Group
import json


def ws_connect(message):
    Group('users').add(message.reply_channel)
    message.reply_channel.send({
        'text': json.dumps({
            'msg': u"你好，很高兴为你服务。",
            'talk': False
        })
    })


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)


def ws_receive(message):
    data = json.loads(message['text'])
    message.reply_channel.send({
        'text': json.dumps({
            'msg': u"我正在思考你的问题{%s}" % data["text"],
            'talk': True
        })
    })
