#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/20

@author: cloudy
'''
from  django.db import models

class Assessment(models.Model):
    '''考核维度'''
    name = models.CharField(max_length=50,verbose_name=u'考核维度',null=False,unique=True)
    mark = models.CharField(max_length=100,verbose_name=u'关键词',null=True,blank=True)
    chief = models.BooleanField(default=False,verbose_name=u'上级评定项')
    level_group = models.ForeignKey('AssessmentLevelGroup', verbose_name=u'评定级别组', null=True, blank=True)


    def __unicode__(self):
        return self.name or ''

    class Meta:
        ordering=['id']
        verbose_name = u'考核维度'
        verbose_name_plural = u'考核维度管理'

class AssessmentLine(models.Model):
    '''考核项'''
    level_group = models.ForeignKey('AssessmentLevelGroup', verbose_name=u'评定级别组', null=True, blank=True)
    assessment = models.ForeignKey(Assessment,verbose_name=u'考核维度',null=False)
    name = models.CharField(max_length=50, verbose_name=u'考核项',null=False,unique=True)
    percent = models.FloatField(default=0, verbose_name=u'权重')
    key_word = models.CharField(max_length=100, verbose_name=u'关键词',null=True,blank=True)
    prompt = models.CharField(max_length=100, verbose_name=u'评价内容')
    max_score = models.IntegerField(default=10, verbose_name=u'最高分')
    min_score = models.IntegerField(default=0, verbose_name=u'最低分')
    active = models.BooleanField(default=True,verbose_name=u'有效')

    def is_chief(self):
        '''是否为上级评定项'''
        return self.assessment.chief



    def __unicode__(self):
        return self.name or ''

    class Meta:
        ordering = ['id']
        verbose_name = u'考核项'
        verbose_name_plural = u'考核项管理'

class AssessmentLineDetail(models.Model):
    '''考核项分级'''
    assessment_line = models.ForeignKey(AssessmentLine,verbose_name=u'考核项',null=False)
    level_group = models.ForeignKey('AssessmentLevelGroup', verbose_name=u'评定级别组', null=True, blank=True)
    level = models.ForeignKey('AssessmentLineLevel',verbose_name=u'评定级别', null=True, blank=True)
    description = models.TextField(verbose_name=u'得分标准',default='' )

    def __unicode__(self):
        result = ""
        if self.assessment_line:
            result = "%s" %  self.assessment_line.name
            if self.level_group:
                result = "%s:%s"%(self.level_group.name,result)
                if self.level:
                    result = "%s(%s)" % ( self.level.name,result)
        return result

    class Meta:
        ordering = ['id']
        verbose_name = u'考核项分级'
        verbose_name_plural = u'考核项分级管理'

class AssessmentLevelGroup(models.Model):
    '''级别组管理'''
    name = models.CharField(max_length=50,verbose_name=u'级别组名称')

    def __unicode__(self):

        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = u'级别组'
        verbose_name_plural = u'级别组管理'


class AssessmentLineLevel(models.Model):
    '''级别明细管理'''
    group = models.ForeignKey(AssessmentLevelGroup,verbose_name=u'级别组')
    sequence = models.IntegerField(default=0,verbose_name=u'序号')
    name = models.CharField(max_length=50,verbose_name=u'分数级别')
    result = models.CharField(max_length=50,verbose_name=u'级别结果')
    max_score = models.FloatField(default=10, verbose_name=u'最高分')
    min_score = models.FloatField(default=0, verbose_name=u'最低分')

    def __unicode__(self):

        return  "%s:%s" %(self.group.name,self.name)

    class Meta:
        ordering = ['id']
        verbose_name = u'级别明细'
        verbose_name_plural = u'级别明细管理'
