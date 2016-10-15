#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/19

@author: cloudy
'''
from  django.conf.urls import url
from . import views

urlpatterns = [
    #绩效首页
    url(r'^index/$',views.index,name='index'),
    #绩效趋势post 请求url
    url(r'^echart/$',views.echart,name='echart'),
    #绩效设置
    url(r'^setting/$',views.setting,name='setting'),
    #绩效考核打分页面
    url(r'^list/$',views.list,name='list'),
    #绩效考核提交
    url(r'^post/$',views.action_post,name='action_post'),
    # 绩效考核提交
    url(r'^check/$', views.check_done, name='check_done'),
    # 历史记录
    url(r'^history/$', views.history, name='history'),
    # 绩效考核详情
    #url(r'^detail/$', views.detail, name='detail'),
    # 绩效考核月度详情
    url(r'^month_detail/$', views.month_detail, name='month_detail'),
    #结果查看
    url(r'^result/$',views.result,name='result'),




]