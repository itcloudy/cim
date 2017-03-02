#!/usr/bin/env python
# coding=utf8
'''
Created on 2016/9/21

@author: cloudy
'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime
import random
SERVER_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

from ..models import  Stakeholder, Record,MonthRecord,Config,ResultCheck,MonthPerformance
from ..common import create_record,create_month_score_record
from base.models import Department

@login_required
def index(request):
    '''绩效首页'''
    context = {}
    context["performanceActive"]= "active"
    user = request.user
    #判断是否有绩效查看的权限
    resultCheck = ResultCheck.objects.filter(user=user)
    if resultCheck:
        resultCheck = resultCheck[0]
        departments = resultCheck.department.all()
        charge_department = Department.objects.filter(charge=request.user)
        charge_department = charge_department and charge_department[0]
        department_id = ''
        if charge_department in departments:
            department_id = charge_department.id
        else:
            department_id = departments[0].id

        return HttpResponseRedirect('/performance/result/?department=%s' % department_id)
    else:
        # 判断是否有未完成的考核
        wait_action = Record.objects.filter(mark__id=user.id, done=False)

        if wait_action:
            context['performInfo'] = True
        month_records = MonthRecord.objects.filter(owner=request.user)
        month_record_list = []
        for month_record in month_records:
            value = {
                'date': month_record.date(),
                'id': month_record.id,
                'score': month_record.score
            }
            if not month_record.done:
                value['score'] = u'未完成'
            month_record_list.append(value)
        if month_record_list:
            context['month_record_list'] = month_record_list
        return render(request, 'performance/index.html', context)


@login_required
def setting(request):
    '''绩效设置'''
    context = {}
    context["performanceActive"]= "active"
    errorList = []
    context['performance_setting'] = True
    if request.method == "POST":
        start_date = request.POST.get('start_date', None)

        if start_date:
            try:
                start_date = datetime.strptime(str(start_date), "%Y/%m/%d %H:%M")
            except:
                errorList.append({'error': u'请输入正确的时间格式'})
        else:
            start_date = datetime.now().strftime(SERVER_DATETIME_FORMAT)
        adjust_time = start_date.strftime("%Y-%m")

        # 判断是否有该月份的考核信息生成
        # date_times = MonthRecord.objects.datetimes('date_time', 'month')
        # time_exsit_list = []
        # for date_time in date_times:
        #     time_exsit_list.append(date_time.strftime("%Y-%m"))
        # if adjust_time in time_exsit_list:
        #     errorList.append({'error': u'%s的考核已经存在' % adjust_time})
        # else:

        # 生成待打分记录信息

        all_stakeholder_list = Stakeholder.objects.all().filter(person__is_active=True)
        print all_stakeholder_list
        exsit_list = []
        #所有的相关人
        for stakeholder in all_stakeholder_list:
            monthPerformance = MonthPerformance.objects.filter(department = stakeholder.person.department,month=adjust_time)
            if monthPerformance:
                monthPerformance = monthPerformance[0]
            else:
                monthPerformance = MonthPerformance(department=stakeholder.person.department, month=adjust_time)
                monthPerformance.save()
            date_times = MonthRecord.objects.filter(owner__id = stakeholder.person.id).datetimes('date_time', 'month')
            time_exsit_list = []
            for date_time in date_times:
                time_exsit_list.append(date_time.strftime("%Y-%m"))
            if adjust_time in time_exsit_list:
                exsit_list.append(stakeholder.person.username_zh)
                continue

            # 创建月份考核信息
            month_record = MonthRecord(
                month = monthPerformance,
                date_time=start_date,
                owner=stakeholder.person
            )
            month_record.save()
            # 批量创建
            bulk_list = []
            # 上级
            highers = stakeholder.higher.all()

            # 相关人
            all_stakeholders = stakeholder.stakeholder.all()
            #部门
            department = stakeholder.person.department
            # 部门考核维度
            config= Config.objects.filter(department=department)
            if config:
                config = config[0]
                department_assessments = config.assessment.all()
                #相关人人数
                random_num = config.random

                if department_assessments:

                    #生成自评
                    create_record(department_assessments, stakeholder.person, stakeholder.person, start_date,month_record, False,True)
                    #生成考核统计结果记录
                    create_month_score_record(department_assessments,month_record,stakeholder.person)

                    # 生成高级相关人待打分记录
                    for higher in highers:
                        create_record(department_assessments, higher, stakeholder.person, start_date, month_record,True,False)
                    com_department_assessments = []

                    for department_assessment in department_assessments:
                        if not department_assessment.chief:
                            com_department_assessments.append(department_assessment)
                    # 生成普通相关人待打分记录
                    if len(all_stakeholders)<= random_num:
                        pass
                    else:
                        all_stakeholders = random.sample(all_stakeholders,random_num)
                    for stakeholder_line in all_stakeholders:
                        create_record(com_department_assessments, stakeholder_line, stakeholder.person, start_date,month_record, False,False)
        if exsit_list:
            errorList.append({'error': u'错误！ %s %s月份的绩效考核已经存在,不再新建' %(','.join(exsit_list),adjust_time)})

    elif request.method == "GET":
        return render(request, 'performance/settings.html', context)
    if errorList:
        context['errorList'] = errorList
        return render(request, 'performance/settings.html', context)
    return render(request, 'base/settings.html', context)