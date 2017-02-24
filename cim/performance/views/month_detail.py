#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/30

@author: cloudy
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from ..models import MonthScore,Record,Stakeholder



@login_required
def month_detail(request):
    '''详情'''
    context= {}
    month_id = request.GET.get('month_id',None)
    data_list = []
    table_title = [u'考核项',u'得分',u'自己']
    if month_id:
        user = request.user

        month_scores = MonthScore.objects.filter(month_record__id =month_id,owner= user)
        stakeholder = Stakeholder.objects.get(person=user)
        highers = stakeholder.higher.all()
        relevants = stakeholder.stakeholder.all()
        higher_len = len(highers)
        relevant_len = len(relevants)
        for i in range(higher_len):
            table_title.append(u'上级%s'% i)
        for i in range(relevant_len):
            table_title.append(u'相关人%s'% i)
        for month_score in month_scores:
            line_list = []
            if not month_score.month_record:
                continue
            assessment_line = month_score.assessment_line
            #考核项
            line_list.append(assessment_line.name)
            #平均分
            line_list.append(month_score.score)
            self_record = Record.objects.get(assessment_line=assessment_line, owner=user, mark=user, month_record= month_score.month_record)
            line_list.append(self_record.score)
            #获得上级的分数
            for higher in highers:
                record = Record.objects.get(assessment_line= assessment_line,owner=user,mark=higher,month_record= month_score.month_record)
                line_list.append(record.score)
            #获得相关人评分
            if assessment_line.assessment.chief:
                for i in range(relevant_len):
                    line_list.append('-')
            else:
                for relevant in relevants:
                    record = Record.objects.all().filter(assessment_line=assessment_line, owner=user, mark=relevant, month_record=month_score.month_record)
                    if len(record)>0:
                        record = record[0]
                        line_list.append(record.score)
            data_list.append(line_list)
    if data_list:
        context['data_list'] = data_list
        context['table_title'] = table_title


    return render(request,'performance/month_detail.html',context=context)