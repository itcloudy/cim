#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/30

@author: cloudy
@description:
'''
from  django.db import models
from .assessment import Assessment



class Config(models.Model):
    '''部门考核配置'''

    department = models.ForeignKey('base.Department',verbose_name=u'部门',unique=True)
    random = models.IntegerField(verbose_name=u'相关人随机数',default=5)
    self_weight = models.FloatField(verbose_name=u'自评权重', default=0, null=True, blank=True)
    higher_weight = models.FloatField(verbose_name=u'上级评分权重', default=0, null=True, blank=True)
    relevant_weight = models.FloatField(verbose_name=u'相关人权重', default=0, null=True, blank=True)
    assessment = models.ManyToManyField(Assessment, verbose_name=u'考核维度',null=True,blank=True)


    def __unicode__(self):
        if self.department:
            return self.department.name
        else:
            return '-'

    class Meta:
        ordering = ['id']
        verbose_name = u'部门考核配置'
        verbose_name_plural = u'部门考核配置管理'