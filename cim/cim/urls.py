#!/usr/bin/env python
#coding=utf8
"""cim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #后台
    url(r'^admin/', include(admin.site.urls)),
    #职业规划
    url(r'^career/',include('career.urls',namespace='career',app_name='career')),
    #绩效考核
    url(r'^performance/', include('performance.urls', namespace='performance', app_name='performance')),
    #基础功能
    url(r'',include('base.urls',namespace='base',app_name='base')),


]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)