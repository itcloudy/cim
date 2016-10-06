#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/16

@author: cloudy
'''
from django.db import models
# from .user import  User



class Position(models.Model):
    '''职位'''


    name = models.CharField(max_length=20,verbose_name=u'职位',null=False,unique=True)
    description = models.TextField(verbose_name=u'职责说明',null=True,blank=True)
    requirements = models.TextField(verbose_name=u'岗位要求', null=True, blank=True)



    def __unicode__(self):
        return self.name or ''

    class Meta:
        verbose_name = u'职位'
        verbose_name_plural = u'职位管理'

