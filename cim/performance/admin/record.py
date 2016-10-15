#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/22

@author: cloudy
@description:
'''
from django.contrib import admin
from ..models import Record,MonthRecord,MonthScore,MonthPerformance


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    '''打分记录后台管理'''
    list_display = ['id','wait_higher','wait_self','month_record','owner','assessment_line','mark','score','done','date_time','mark_time']
    list_filter = ['month_record','mark','owner','assessment_line','done']
    search_fields = ['owner']


@admin.register(MonthRecord)
class MonthRecordAdmin(admin.ModelAdmin):
    '''打分记录后台管理'''
    list_display = ['name','month','date_time','owner', 'done','score']
    list_filter = ['owner','done']
    search_fields = ['owner']

@admin.register(MonthScore)
class MonthScoreAdmin(admin.ModelAdmin):
    "月度考核结果后台管理"
    list_display = ['month_record','owner','assessment_line','done','score']
    list_filter = ['month_record', 'owner']

@admin.register(MonthPerformance)
class MonthPerformanceAdmin(admin.ModelAdmin):
    "月份后台管理"
    list_display = ['month','department']
    list_filter = ['month','department']