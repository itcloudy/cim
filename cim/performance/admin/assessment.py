#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/20

@author: cloudy
'''
from django.contrib import admin
from ..models import Assessment,AssessmentLine,AssessmentLineDetail,AssessmentLineLevel,AssessmentLevelGroup


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    '''考核维度后台管理'''
    list_display = ['name','level_group','chief', 'mark']
    search_fields = ['name']
    actions = ['setChiefAction','unsetChiefAction']

    def setChiefAction(self,request,queryset):
        '''设置为上级评定项'''
        queryset.update(chief=True)

    setChiefAction.short_description =u'设置为上级评定项'
    def unsetChiefAction(self,request,queryset):
        '''设置为普通评定项'''
        queryset.update(chief=False)

    unsetChiefAction.short_description = u'设置为普通评定项'

@admin.register(AssessmentLine)
class AssessmentLineAdmin(admin.ModelAdmin):
    '''考核项后台管理'''

    list_display = ['name','assessment','level_group','active','prompt','percent','max_score','min_score','key_word']
    list_filter = ['assessment','active','level_group']
    search_fields = ['name','assessment']
    actions = ['setDisable', 'setActive']

    def setDisable(self, request, queryset):
        '''设置为无效'''
        queryset.update(active=False)

    setDisable.short_description = u'设置为无效'

    def setActive(self, request, queryset):
        '''设置为有效'''
        queryset.update(active=True)

    setActive.short_description = u'设置为有效'

@admin.register(AssessmentLineDetail)
class AssessmentLineDetailAdmin(admin.ModelAdmin):
    '''考核项分级后台管理'''
    list_display = ['assessment_line','level','description']
    list_filter = ['assessment_line','level_group']
    search_fields = ['assessment_line']


@admin.register(AssessmentLevelGroup)
class AssessmentLevelGroupAdmin(admin.ModelAdmin):
    '''级别组后台管理'''
    list_display = ['name']

@admin.register(AssessmentLineLevel)
class AssessmentLineLevelAdmin(admin.ModelAdmin):
    '''级别明细后台管理'''
    list_display = ['name','sequence', 'result', 'max_score', 'min_score','group']