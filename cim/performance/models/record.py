#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/21

@author: cloudy
'''
from  django.db import  models
from .assessment import AssessmentLine
from datetime import datetime



class MonthRecord(models.Model):
    '''月度考核'''
    def __unicode__(self):
        if self.date_time:
            return self.date_time.strftime("%Y/%m")
        else:
            return '-'

    class Meta:
        ordering = ['id']
        verbose_name = u'月度考核'
        verbose_name_plural = u'月度考核管理'


    date_time = models.DateTimeField(verbose_name=u'开始时间', null=True, blank=True)
    owner = models.ForeignKey('base.User', related_name='month_record_owner', verbose_name=u'得分人', null=False)
    done = models.BooleanField(verbose_name=u'完成', default=False)
    score = models.FloatField(default=-1, verbose_name=u'总分')
    def name(self):
        '''名称'''
        if self.date_time:
            result =  self.date_time.strftime("%Y/%m")
            if result:
                return "%s(%s)"%(self.owner,result)
        return '-'
    name.short_description = u"名称"
    name_str = property(name)
    def date(self):
        '''获得月份'''
        if self.date_time:
            return self.date_time.strftime("%Y/%m")
        return '-'

class MonthScore(models.Model):
    '''月度考核结果'''
    month_record = models.ForeignKey(MonthRecord,verbose_name=u'考核月份',null=True,blank=True)
    owner = models.ForeignKey('base.User',related_name='month_score_owner',verbose_name=u'得分人',null=True,blank=True)
    assessment_line = models.ForeignKey(AssessmentLine, verbose_name=u'考核项', null=True,blank=True)
    score = models.FloatField(verbose_name=u'平均分',default=0)
    done = models.BooleanField(verbose_name=u'完成', default=False)
    class Meta:
        ordering = ['month_record','owner','id']
        verbose_name = u'月度考核结果'
        verbose_name_plural = u'月度考核结果管理'
    def name(self):
        '''名称'''
        if self.month_record and self.owner:
                return "%s(%s)"%(self.month_record.name,self.owner.username_zh)
        return '-'

class Record(models.Model):
    """打分记录"""
    month_record = models.ForeignKey(MonthRecord,verbose_name=u'月份')
    assessment_line = models.ForeignKey(AssessmentLine,verbose_name=u'考核项',null=False)
    wait_higher = models.BooleanField(verbose_name=u'上级打分项',default=False)
    wait_self = models.BooleanField(verbose_name=u'自评项',default=False)
    owner = models.ForeignKey('base.User',related_name='record_owner',verbose_name=u'得分人',null=False)
    mark = models.ForeignKey('base.User',related_name='record_mark',verbose_name=u'打分人',null=True,blank=True)
    score = models.FloatField(default=0,verbose_name=u'得分')
    date_time = models.DateTimeField(verbose_name=u'开始时间',null=True,blank=True)
    mark_time = models.DateTimeField(verbose_name=u'打分时间',null=True,blank=True)
    done = models.BooleanField(verbose_name=u'完成',default=False)
    def __unicode__(self):
        if self.owner:
            name = "%s:%s"% (self.owner.username_zh,self.assessment_line.name)
            return name
        else:
            return '-'

    class Meta:
        verbose_name = u'打分记录'
        verbose_name_plural = u'打分记录管理'

