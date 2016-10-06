#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/21

@author: cloudy
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.contrib import auth
from django.http import HttpResponseRedirect



@login_required
def index(request):
    '''职业规划首页'''
    context = {}
    return  render(request,'career/index.html',context)