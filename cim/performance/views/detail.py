#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/30

@author: cloudy
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required



@login_required
def detail(request):
    '''详情'''
    context= {}
    return render(request,'performance/detail.html',context=context)