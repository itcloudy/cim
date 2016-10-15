#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/30

@author: cloudy
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from ..models import  MonthRecord,MonthScore


@login_required
def history(request):
    '''详情'''
    context= {}
    user = request.user
    month_records = MonthRecord.objects.filter(owner=user)
    month_record_list = []
    table_title_list = [u'月份',u'总分']
    table_title_flag =True
    for month_record in month_records:
        value = {
            'date': month_record.date(),
            'id': month_record.id,
            'data':[],
        }
        if not month_record.done:
            value['score'] = u'未完成'
        month_scores = MonthScore.objects.filter(month_record = month_record,owner=user)
        value['data'].append(month_record.score)
        for month_score in month_scores:
            value['data'].append(month_score.score)
            if table_title_flag:
                title = "%s(%s)%%"%(month_score.assessment_line.name,month_score.assessment_line.percent)
                table_title_list.append()
        table_title_flag = False
        month_record_list.append(value)

    if month_record_list:
        context['table_title_list'] = table_title_list
        context['month_record_list'] = month_record_list
    return render(request,'performance/history.html',context=context)