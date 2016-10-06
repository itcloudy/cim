#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/17

@author: cloudy
'''
from django.db import  models
from user import User


class Team(models.Model):
    '''团队'''


    name = models.CharField(max_length=20,verbose_name=u'团队名称',null=False,unique=True)
    member = models.ManyToManyField(User,verbose_name=u"团队成员")
    is_active = models.BooleanField(default=True,verbose_name=u"团队有效")
    def __unicode__(self):
        return self.name or ""

    class Meta:
        verbose_name = u'团队'
        verbose_name_plural = u'团队管理'
