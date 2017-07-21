# -*- coding: UTF-8 -*-
from django.conf.urls import url
from example.views import chat

urlpatterns = [
    url(r'^$', chat, name='chat'),
]