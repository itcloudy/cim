#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/22

@author: cloudy
@description:相关人设置
'''
from  django.db import models


class Stakeholder(models.Model):
    '''相关人'''

    person = models.ForeignKey('base.User', related_name='person',verbose_name=u'拥有者',unique=True)
    higher = models.ManyToManyField('base.User',related_name='higher',verbose_name=u'高级相关人',null=True,blank=True)
    stakeholder = models.ManyToManyField('base.User',related_name='stakeholder',verbose_name=u'普通相关人',null=True,blank=True)

    def is_active(self):
        '''有效'''
        if  self.person.is_active:

            return u'有效'
        else:
            return u'无效'
    is_active.short_description = u"有效"
    is_active_str = property(is_active)
    def __unicode__(self):
        if self.person:

            return self.person.username_zh
        else:
            return '-'

    class Meta:
        verbose_name = u'相关人'
        verbose_name_plural = u'相关人管理'


