#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/23

@author: cloudy
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

from base.models import  Department,Position,User

@login_required
def add_user(request):
    '''用户添加'''
    context = {}
    context['add_user'] = True
    if request.method == 'GET':
        #获得职位信息
        positions = Position.objects.all()
        position_list = []
        for position in positions:
            position_list.append({
                'id': position.id,
                'name': position.name,
            })
        #获得部门信息
        departments = Department.objects.all()
        department_list = []
        for department in departments:
            department_list.append({
                'id': department.id,
                'name': department.name,
            })
        if department_list:
            context['department_list'] = department_list
        if position_list:
            context['position_list'] = position_list

    else:
        errorList = []
        username = request.POST['username']
        username_zh = request.POST.get('username_zh','')
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        department = request.POST.get('department','')
        position = request.POST.get('position','')
        chief = request.POST.get('chief','')
        short_phone = request.POST.get('short_phone','')
        if password != confirm_password:
            errorList.append({'error': u'密码不一致'})
        else:
            user = User( )
            if username:
                user.username =username
            if username_zh:
                user.username_zh = username_zh
            if mobile:
                user.mobile = mobile
            if department:
                user.department = Department.objects.get(id=int(department))
            if position:
                user.position = Position.objects.get(id=int(position))
            if short_phone:
                user.short_phone = short_phone
            user.set_password(password)
            try:
                user.full_clean()
                user.save()

            except ValidationError as e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programmatically.
                errKeys = e.message_dict.keys()
                for errKey in errKeys:
                    errorList.append({'error':e.message_dict[errKey][0]})
        if errorList:
            context['errorList'] = errorList

    return render(request, 'base/settings.html', context)