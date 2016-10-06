#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/19

@author: cloudy
'''

from django import forms

class loginForm(forms.Form):
    '''登录表单'''
    username  = forms.CharField(max_length=20,label=u"用户名",required=True)
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput,required=True)