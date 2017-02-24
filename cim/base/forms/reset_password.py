#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/20

@author: cloudy
'''
from django import forms

class resetPasswordForm(forms.Form):
    '''修改密码'''
    username = forms.CharField(widget=forms.TextInput,label=u'用户名',required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, label=u'新密码', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label=u'确认密码', required=True)