#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.

class TempLog(models.Model):
	temperature = models.FloatField()
	recv_time = models.DateTimeField('receive time')
	
	def was_received_recently(self):
		now = timezone.now()
		return now >= self.recv_time >= timezone.now() - datetime.timedelta(days=1)


		
