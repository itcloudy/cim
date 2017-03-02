#!/usr/bin/env python
# encoding: utf-8
"""
@project:ProjectCIM
@author:cloudy
@site:
@file:result.py
@date:2016/10/14 10:16
"""
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from ..models import MonthRecord,MonthScore,Record,ResultCheck
from ..models import Config, MonthPerformance,AssessmentLine
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
import json
from base.models import Department
@csrf_protect
@login_required
def result(request):
    '''查看结果'''
    context = {}
    context["performanceActive"]= "active"
    user = request.user
    wait_action = Record.objects.filter(mark__id=user.id, done=False)
    department_list = []
    month_list = []
    if request.method =="GET":
        if wait_action:
            context['performInfo'] = True
        page = request.GET.get('page','1')
        department_id = request.GET.get('department','')
        name = request.GET.get('name','')
        page = page and int(page)
        month= request.GET.get('month','')
        month = month and int(month)
        department_id = department_id and int(department_id)
        cur_department = Department.objects.get(id=department_id)
        department_list.append({'id': cur_department.id, 'name': cur_department.name})
        monthPerformances = MonthPerformance.objects.filter(department=cur_department)
        for monthPerformance in monthPerformances:
            month_list.append({
                'name': monthPerformance.month
            })
        resultCheck = ResultCheck.objects.get(user = user)
        departments = resultCheck.department.all()
        for department in departments:
            if department != cur_department:
                department_list.append({'id':department.id,'name':department.name})
        result_data = search_result(department_id, month_id=month, name=name, page=page)
        if result_data:
            context['result_data'] = result_data
        context['department_list'] = department_list
        context['month_list'] = month_list
        context['cur_department'] = department_id
        context['month'] = month
        context['name'] = name
        return render(request, 'performance/result.html', context=context)
    elif request.method == 'POST':
        response_dict = {
            'code': '500',
            'msg': '',
        }
        department_id = request.POST.get('department', '')
        name = request.POST.get('name', '')
        month = request.POST.get('month', '')
        month = month and int(month)
        department_id = department_id and int(department_id)
        cur_department = Department.objects.get(id=department_id)
        department_list.append({'id': cur_department.id, 'name': cur_department.name})
        monthPerformances = MonthPerformance.objects.filter(department__id=department_id)
        for monthPerformance in monthPerformances:
            month_list.append({
                'id':monthPerformance.id,
                'name': monthPerformance.month
            })
        resultCheck = ResultCheck.objects.get(user=user)
        departments = resultCheck.department.all()
        for department in departments:
            if department != cur_department:
                department_list.append({'id': department.id, 'name': department.name})
        result_data = search_result(department_id, month_id=month, name=name, page=1)
        if 'table_list' in result_data.keys():
            response_dict['code']='200'
            response_dict['result_data'] = result_data
            response_dict['month_list'] = month_list
        return HttpResponse(json.dumps(response_dict, ensure_ascii=False), content_type="application/json")

def search_result(department_id,month_id=0,name='',page=1):
    config = Config.objects.filter(department__id=department_id)
    result_data = {}
    if config:
        config = config[0]
        assessments = config.assessment.all()
        assessmentLines = AssessmentLine.objects.filter(assessment__in=assessments)
        assessment_line_ids = [line.id for line in assessmentLines]
        table_title = [u'月份', u'得分人', u'总分']
        table_title += [line.name for line in assessmentLines]
        table_title.append(u"详情")

        table_list = []
        monthRecords = MonthRecord.objects.filter(owner__department__id=department_id)
        if name:
            full_monthRecords = monthRecords.filter(owner__username_zh=name)
            if full_monthRecords:
                monthRecords = full_monthRecords
            else:
                monthRecords = monthRecords.filter(owner__username_zh__contains=name)
        if month_id:
            monthRecords = monthRecords.filter(month__id=month_id)
        paginator = Paginator(monthRecords, 20)
        all_page = paginator.num_pages
        if page > all_page:
            page = all_page
        if page < 1:
            page = 1

        monthRecords = paginator.page(page)
        result_data['current_page'] = page
        result_data['all_page'] = all_page
        if page >1:
            result_data['previous'] = page-1
        if page < all_page:
            result_data['next'] = page + 1

        for monthRecord in monthRecords.object_list:
            tem_list = [monthRecord.month.month, monthRecord.owner.username_zh]
            if monthRecord.done:
                tem_list.append(monthRecord.score)
            else:
                tem_list.append(u'未完成')
            for assessment_line_id in assessment_line_ids:
                monthScore = MonthScore.objects.get(month_record=monthRecord, owner=monthRecord.owner,
                                                    assessment_line__id=assessment_line_id)
                if monthScore.done:
                    tem_list.append(monthScore.score)
                else:
                    tem_list.append(u'未完成')
            tem_list.append(monthRecord.id)
            table_list.append(tem_list)
        if table_list:
            result_data['table_title'] = table_title
            result_data['table_list'] = table_list
            result_data['department_id'] =department_id
            result_data['month_id'] =month_id
            result_data['name'] =name

    return result_data



