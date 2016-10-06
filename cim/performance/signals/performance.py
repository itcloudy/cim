#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/24

@author: cloudy
@description:
'''
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import AssessmentLineDetail

@receiver(pre_save,sender=AssessmentLineDetail)
def add_group_info(sender,instance,*args,**kwargs):
    ''''''
    if instance and instance.level:
        instance.level_group = instance.level.group



