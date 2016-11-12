#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-12 01:04:50
# @Author  : Alex Tang (1174779123@qq.com)
# @Link    : http://t1174779123.iteye.com
'''
	description:
'''

from django.conf.urls import url 
from . import views

app_name = 'charts'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^/input/$', views.input, name = 'input'),
	url(r'^/result/$', views.result, name = 'result'),
	url(r'^/addDate/$', views.addDate, name = 'addDate'),
	
]

