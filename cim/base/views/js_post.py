#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/23

@author: cloudy
@description:
'''
from django.views.decorators.csrf import csrf_protect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import  login_required
from base.models import  Department,Position

import json

@csrf_protect
@login_required
def js_post(request,route=''):
    '''javascript请求转发'''
    response_dict = {
        'code': '500',
        'msg': '',
    }
    if request.method =='POST':
        if not route:
            response_dict['msg'] = u'请求参数不全'
        elif 'department'== route:
            response_dict = get_departmant(request)
        elif 'position'== route:
            response_dict = get_position(request)
    else:
        response_dict['msg'] = u'请求使用post请求'
    return HttpResponse(json.dumps(response_dict, ensure_ascii=False), content_type="application/json")
def get_departmant(request):
    '''获得部门信息'''
    response_dict = {
        'code':'500',
        'msg':'',

    }
    departments = Department.objects.all()
    key = request.POST.get('key','')
    if key:
        departments =departments.filter(name__contains= key)
    department_list = []
    for department in departments:
        department_list.append({
            'id':department.id,
            'name':department.name,
        })
    if department_list:
        response_dict['code'] = '200'
        response_dict['data'] = department_list
    return  response_dict
def get_position(request):
    '''获得职位信息'''
    response_dict = {
        'code': '500',
        'msg': '',

    }
    positions = Position.objects.all()
    key = request.POST.get('key', '')
    if key:
        positions = positions.filter(name__contains=key)
    position_list = []
    for position in positions:
        position_list.append({
            'id': position.id,
            'name': position.name,
        })
    if position_list:
        response_dict['code'] = '200'
        response_dict['data'] = position_list
    return response_dict