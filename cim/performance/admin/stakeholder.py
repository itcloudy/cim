#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/22

@author: cloudy
@description:
'''
from django.contrib import admin
from ..models import Stakeholder,ResultCheck

@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    '''相关人后台设置'''
    list_display = ['person','is_active']
    list_filter = ['person','higher','stakeholder']
    filter_horizontal = ['higher','stakeholder']


@admin.register(ResultCheck)
class CheckResultAdmin(admin.ModelAdmin):
    '''结果查看人管理'''
    list_display = ['user']
    filter_horizontal = ['department' ]