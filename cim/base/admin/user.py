#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/16

@author: cloudy
'''

from django.contrib import admin

from ..models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''用户后台信息管理'''
    search_fields = ['username','mobile','department','position']
    list_display = ['username','username_zh','department','chief','short_phone','position','mobile','is_active']
    list_filter = ['department', 'position']

    fieldsets = [
        (u'基本信息',{
            'classes': ['collapse'],
            'fields':['username','username_zh','is_active','email','mobile','short_phone'],
        }),
        (u'部门信息', {
            'classes': ['collapse'],
            'fields': [ 'department','position','chief'],
        }),
    ]
    actions = ['setDisable','setActive']
    def setDisable(self,request,queryset):
        '''设置用户无效'''
        queryset.update(is_active=False)

    setDisable.short_description = u'设置用户无效'
    def setActive(self,request,queryset):
        '''设置用户有效'''
        queryset.update(is_active=True)

    setActive.short_description = u'设置用户有效'

