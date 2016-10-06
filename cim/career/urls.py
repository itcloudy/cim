#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/19

@author: cloudy
'''
from  django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index/$',views.index,name='index'),

]