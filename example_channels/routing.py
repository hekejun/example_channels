# -*- coding: UTF-8 -*-
"""
File: routing.py 
Created since 2017/7/20 11:32.
Author: Kejun.He
"""
from channels.routing import route
from example.consumers import ws_connect, ws_disconnect,ws_receive


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_receive),
    route('websocket.disconnect', ws_disconnect),
]