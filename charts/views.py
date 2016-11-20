#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.core import serializers
import json,time

from .models import TempLog
# Create your views here.
show_date_num = 100
#首页
def index(request):
	return render(request, 'charts/index.html')
#输入数据页
def input(request):
	return render(request, 'charts/input.html')
#数据结果页
def result(request):
	latest_templog_list = TempLog.objects.order_by('-recv_time')[:show_date_num]
	context = {'latest_templog_list':latest_templog_list}
	return render(request, 'charts/result.html',context)
#处理数据
def addData(request):
	print request.POST
	temp = float(request.POST['temp'])
	print 'get temp',temp
	time_stamp = int(time.mktime(timezone.now().timetuple()))
	templog = TempLog(temperature=temp, recv_time=timezone.now(), recv_timestamp = time_stamp)
	templog.save()
	return HttpResponseRedirect(reverse('charts:result'))

#处理wifi模块数据
def addWifiData(request):
	print request.POST
	temp = float(request.POST['temp'])
	print 'get wifi temp',temp
	time_stamp = int(time.mktime(timezone.now().timetuple()))
	templog = TempLog(temperature=temp, recv_time=timezone.now(), recv_timestamp = time_stamp)
	templog.save()
	return HttpResponse('<h1>get wifi temp </h1>')

#显示温度数据页面
def showData(request):
	#TODO: 能否只返回两个字段
	temp_list = TempLog.objects.order_by('recv_time')
	temp_datas = getJsonData(temp_list)
	# temp_datas = serializers.serialize('json',temp_list)
	print 'length: ',len(temp_datas)
	context = {'temp_datas':json.dumps(temp_datas)}
	return render(request, 'charts/showdata.html', context)
#由QuerySet得到Json数据的子函数
def getJsonData(temp_list):
	temp_datas = []
	for templog in temp_list:
		# temp_data = {'time':time_stamp,
		# 			 'temperature':templog.temperature}
		temp_data = [templog.recv_timestamp*1000, templog.temperature]
		temp_datas.append(temp_data)
	return temp_datas

#向前端返回更新数据的方法
def sendUpdateData(request):
	if request.method == 'POST':
		print request.POST
		latest_time = int(request.POST['latest_time'])/1000
		print 'POST from JS , latest_time = ',latest_time
		#查询数据库得到更新的数据
		new_list = TempLog.objects.filter(recv_timestamp__gt=latest_time)
		print "new_list:",len(new_list)
		new_data = getJsonData(new_list)
		#返回数据给前端
		return HttpResponse(json.dumps(new_data))



