#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/21

@author: cloudy
'''

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import  login_required
from django.http.response import HttpResponse
import json
from ..models import  MonthRecord,Record,Stakeholder,MonthScore,Config


@csrf_protect
def echart(request):
    '''趋势请求'''
    response_dict={
        'code':'500',
        'data':[],
        'type':'',
    }
    if request.method == "POST":
        style = request.POST.get('style','')
        if style =='trend':
            response_dict = get_trend(request)
        elif style == 'detail':
            response_dict['code'] ='200'

    return HttpResponse(json.dumps(response_dict, ensure_ascii=False), content_type="application/json")

def get_trend(request):
    '''获得趋势图'''
    response_dict = {
        'code': '200',
    }
    user = request.user
    legend_data = []
    xAxis_data = []
    yAxis_left_data = [line for line in range(10)]
    series = {}
    stakeholders = Stakeholder.objects.filter(person=user)
    #如果存在相关人
    if stakeholders:

        month_records = MonthRecord.objects.filter(owner=user,done=True)
        if month_records:
            legend_data=[u'总分']
            series[u'总分'] = {
                'name':u'总分',
                'type':'line',
                'stack':u'总量',
                'data':[],
            }
            #获得标题完成和考核项list完成标志
            top_data_flag =True

            #获得所有的月份数据
            for month_record in month_records:
                #总分序列
                series[u'总分']['data'].append(month_record.score)

                xAxis_data.append(month_record.date())

                month_scores  = MonthScore.objects.filter(month_record=month_record,owner=user)
                for month_score in month_scores:
                    if top_data_flag:
                        legend_data.append(month_score.assessment_line.name)
                        # series[month_score.assessment_line.name]={
                        #     'name':month_score.assessment_line.name,
                        #     'type':'bar',
                        #     'stack':u'总量',
                        #     'data':[],
                        # }
                    # series[month_score.assessment_line.name]['data'].append(month_score.score)


                top_data_flag = False
        response_dict['legend_data'] = legend_data
        response_dict['xAxis_data'] = xAxis_data
        response_dict['yAxis_left_data'] = yAxis_left_data
        response_dict['series'] = series.values()

    return response_dict