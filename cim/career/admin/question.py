#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/21

@author: cloudy
'''
from django.contrib import admin

from ..models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''问题后台管理'''
    list_display = ['name','key_word']