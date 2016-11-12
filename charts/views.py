#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import TempLog
# Create your views here.
show_date_num = 100
#首页
def index(request):
	return HttpResponse(u'这是主页！！')
#输入数据页
def input(request):
	return render(request, 'charts/input.html')
#数据结果页
def result(request):
	latest_templog_list = TempLog.objects.order_by('-recv_time')[:show_date_num]
	context = {'latest_templog_list':latest_templog_list}
	return render(request, 'charts/result.html',context)
#处理数据
def addDate(request):
	temp = float(request.POST['temp'])
	templog = TempLog(temperature=temp, recv_time=timezone.now())
	templog.save()
	return HttpResponseRedirect(reverse('charts:result'))