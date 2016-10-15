#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/17

@author: cloudy
'''
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from ..forms import loginForm,passForm
from .user import *
from base.models import  User


def index(request):
    '''首页'''
    context = {}
    if 'user' in request.session.keys():
        context['user'] =request.session['user']

    return  render(request,'base/index.html',context)

def login(request):
    '''登录'''
    context = {}
    if request.method == "POST":
        formLogin = loginForm(request.POST)
        if formLogin.is_valid():
            username = formLogin.data['username']
            password = formLogin.data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                else:
                    context['error'] = u"无效用户"
            else:
                context['error'] = u"用户名或密码错误"
        else:
            context['error'] = u"用户名或密码错误"
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

@login_required
def logout(request):
    '''注销登录'''
    if 'user' in request.session.keys():
        del request.session['user']
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def settings(request,style=''):
    '''设置'''

    context = {}
    if not style or style =='index':
        pass
    elif style == 'change_password':

        return change_password(request)
    elif style == 'add_user':

        return  add_user(request)
    return render(request, 'base/settings.html', context)

@login_required
def change_password(request):
    '''修改密码'''
    context = {}
    context['change_password'] = True
    errorList  = []
    if request.method == "POST":
        pForm = passForm(request.POST)
        if pForm.is_valid():
            old_password = pForm.data['old_password']
            new_password = pForm.data['new_password']
            confirm_password = pForm.data['confirm_password']
            if new_password != confirm_password:
                errorList.append( {'error':u'密码不一致'})
            else:
                user = User.objects.get(id=request.user.id)
                if user.check_password(old_password):
                    if str( user.username ) ==str(confirm_password):
                        errorList.append({'error': u'密码不能和用户名相同'})
                    else:
                        user.set_password(confirm_password)
                        user.save()
                        logout(request)
                        return HttpResponseRedirect('/')
                else:
                    errorList.append({'error':u'旧密码不对'})
        if errorList:
            context['errorList'] = errorList
        return render(request, 'base/settings.html', context)
    else:
        return render(request, 'base/settings.html', context)





