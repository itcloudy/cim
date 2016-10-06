#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/19

@author: cloudy
@desc:七问
'''
from  django.db import models

class Question(models.Model):
    '''问题'''
    name = models.TextField(verbose_name=u'问题')
    key_word = models.TextField(verbose_name=u'关键信息')
    def __unicode__(self):
        return self.name or ''

    class Meta:
        verbose_name = u'问题'
        verbose_name_plural = u'问题管理'