#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/23

@author: cloudy
@description:
'''
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect
from ..models import Record,AssessmentLine,AssessmentLineLevel,AssessmentLineDetail
import math
from  datetime import  datetime
from ..models import MonthRecord,Config,Stakeholder,MonthScore
from base.models import User
from ..common import mean,average
SERVER_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@login_required
def list(request):
    '''考核打分'''
    context = {}

    user_id = request.GET.get('user_id','0')
    user_id = int(user_id)
    if user_id:
        context['user_id'] = user_id
    detail = request.GET.get('detail',None)
    error = request.GET.get('error','')
    if 'scoreInvalid' ==error:
        context['error'] = u"分数必须大于等于0小于等于10"
    #获得评定内容
    if detail:
        context['details'] = performance_form(request,request.user.id)
    #判断是否有自评未完成
    self_records = Record.objects.filter(done=False,owner__id=request.user.id,mark__id=request.user.id)
    if self_records:
        context['self_record'] = True
        # 获得某个人的评定项
        if user_id==request.user.id:
            context['performance_details'] = performance_form(request, user_id)

    #判断是否有下级评定项
    lower_records = Record.objects.filter(wait_higher=True,done=False,mark__id=request.user.id)
    lower_list = []
    lower_owner_list = []
    for lower_record in lower_records:
        low_owner_id = lower_record.owner.id
        if low_owner_id not in lower_owner_list:
            lower_owner_list.append(low_owner_id)
            lower_list.append({'id': low_owner_id, 'name': lower_record.owner.username_zh})
        # 获得某个人的评定项
        if user_id ==lower_record.owner.id:
            context['performance_details'] = performance_form(request, user_id)

    context['lower_mark_list'] = lower_list

    #判断是否有相关人评定项
    stakeholder_records = Record.objects.filter(wait_higher=False,done=False, mark__id=request.user.id).exclude(owner__id=request.user.id)
    stakeholder_list = []
    stakeholder_owner_list = []
    for stakeholder_record in stakeholder_records:
        owner_id = stakeholder_record.owner.id
        if owner_id not in stakeholder_owner_list:
            stakeholder_owner_list.append(owner_id)
            stakeholder_list.append({'id':owner_id,'name':stakeholder_record.owner.username_zh})
        #获得某个人的评定项
        if user_id ==stakeholder_record.owner.id:
            context['performance_details'] = performance_form(request, user_id)


    context['stakeholder_list'] =stakeholder_list
    #获得已经完成的月度考核
    return render(request, 'performance/action.html', context)



def performance_form(request,user_id):
    ''''生成评定表单'''

    #考核项
    result = []
    if not user_id:
        return  result
    user = User.objects.get(id=user_id)
    department = user.department
    if department:
        config = Config.objects.filter(department=department)
        if config:
            config = config[0]
            assessments = config.assessment.all()
            if assessments:
                for assessment in assessments:
                    if request.user.id != user_id:
                        #判断是否为上级评定项
                        if assessment.chief:
                            #获得该用户的上级评定项
                            stakeholder = Stakeholder.objects.filter(person__id = user_id)
                            if stakeholder:
                                stakeholder = stakeholder[0]
                                highers = stakeholder.higher.all()
                                higher_ids = [line.id for line in highers]
                                if request.user.id not in higher_ids:
                                    continue
                            else:
                                continue


                    assessment_dict = {}
                    assessment_dict['name'] = assessment.name or "-"
                    title= {}
                    assessment_lines = AssessmentLine.objects.filter(assessment = assessment)
                    levels = AssessmentLineLevel.objects.filter(group  = assessment.level_group)
                    #生成评定项头部信息
                    for level in levels:
                        title[level.sequence] = level.name or "-"
                    title_list = []
                    title_keys = title.keys()
                    title_keys.sort(reverse=True)
                    for title_key in title_keys:
                        title_list.append(title[title_key])
                    assessment_dict['title_list'] = title_list

                    #生成评定项明细
                    assessment_line_list = []
                    for assessment_line in assessment_lines:
                        line_dict = {}
                        line_dict['name'] = "%s(%s%)"%(assessment_line.name or "-",assessment_line.percent)

                        #获得已经保存的分数
                        record = Record.objects.filter(done=False,owner=user,assessment_line=assessment_line,mark=request.user)
                        if record:
                            record = record[0]
                            line_dict['record_id']='record_%s' %record.id

                            line_dict['value'] = record.score
                        line_dict['prompt'] = assessment_line.prompt or "-"
                        line_dict['key_word'] = assessment_line.key_word or "-"
                        line_detail_dict = {}
                        line_details = AssessmentLineDetail.objects.filter(assessment_line =assessment_line)
                        for detail in line_details:
                            line_detail_dict[detail.level.sequence] = detail.description
                        #排序
                        keys = line_detail_dict.keys()
                        keys.sort(reverse=True)
                        line_detail_list = []
                        for key in keys:
                            line_detail_list.append(line_detail_dict[key])
                        line_dict['detail_list'] = line_detail_list
                        assessment_line_list.append(line_dict)
                    assessment_dict['assessment_line_list'] =assessment_line_list
                    assessment_dict['table_rowspan'] = len(assessment_line_list)
                    result.append(assessment_dict)


    return  result


@login_required
def action_post(request):
    '''数据提交'''
    postParamKeys = request.POST.keys()
    not_done = request.POST.get('not_done','')
    done = True
    if not_done:
        done = False
    user_id = None
    error = False
    done_list = []
    for postParamKey in postParamKeys:
        if 'record' in postParamKey:
            record_id = postParamKey.split('_')[1]
            done_list.append(record_id)
            record_id = int(record_id)
            record = Record.objects.get(id=record_id)
            user_id = record.owner.id
            score = float(request.POST.get(postParamKey,0))
            ad_score = round(score,1)
            if done:
                if ad_score>10 or ad_score<0:
                    error =True
                    break
            record.score = ad_score
            record.mark_time =  datetime.now().strftime(SERVER_DATETIME_FORMAT)
            record.save()
    if not error and done:
        Record.objects.filter(id__in=done_list).update(done=True)
    #临时保存返回原来的页面
    if (not_done or error) and user_id:
        url = '/performance/list/?user_id=%s' % user_id
        if error:
            url  = "%s&error=scoreInvalid" % url
        return HttpResponseRedirect(url)
    #非临时提交保存,返回json数据
    if user_id:
        return HttpResponseRedirect('/performance/check/?user_id=%s' % user_id)
    return HttpResponseRedirect('/performance/list/?detail=1')


@login_required
def check_done(request):
    '''检测是否完成'''
    user_id = request.GET.get('user_id', '0')
    if user_id:
        month_records = MonthRecord.objects.filter(owner__id = user_id,done=False)
        user = User.objects.get(id=user_id)
        config = Config.objects.get(department = user.department)
        self_weight = config.self_weight
        higher_weight = config.higher_weight
        relevant_weight = config.relevant_weight
        assessments = config.assessment.all()
        assessment_line_percent_dict={}


        for month_record in month_records:
            # 保存不同人员的打分结果
            #自己
            self_assessment_line_dict = {}
            #上级
            higher_assessment_line_dict = {}
            #相关人
            relevant_assessment_line_dict = {}
            assessment_line_list = []

            records = Record.objects.filter(owner__id = user_id,month_record=month_record,done=False)
            #如果不存在，则说明所有的评分已经完成
            if not records:
                month_record.done = True


                for assessment in assessments:
                    assessment_lines = AssessmentLine.objects.filter(assessment__id=assessment.id)
                    for assessment_line in assessment_lines:
                        assessment_line_percent_dict[assessment_line.id] = assessment_line.percent
                        assessment_line_list.append(assessment_line.id)
                        #获得自评的分数
                        self_records = Record.objects.filter(
                            owner__id = user_id,
                            month_record=month_record,
                            wait_self=True,assessment_line=assessment_line)
                        self_assessment_line_dict[assessment_line.id] = [float(self_line.score) for self_line in self_records]
                        #获得上级评分分数
                        higher_records = Record.objects.filter(
                            owner__id=user_id,
                            month_record=month_record,
                            wait_higher=True, assessment_line=assessment_line)
                        higher_assessment_line_dict[assessment_line.id] = [float(higher_line.score) for higher_line in higher_records]
                        #获得相关人评分分数
                        relevant_records = Record.objects.filter(
                            owner__id=user_id,
                            month_record=month_record,
                            wait_higher=False,wait_self=False, assessment_line=assessment_line)
                        relevant_assessment_line_dict[assessment_line.id] = [float(relevant_line.score) for relevant_line in
                                                                          relevant_records]
                #考核总分
                total_score = 0
                all_percent = 0
                #对打分结果进行统计
                if assessment_line_list:
                    for assessment_line_id in assessment_line_list:

                        self_score = average(self_assessment_line_dict.get(assessment_line_id,[]))
                        higher_score = average(higher_assessment_line_dict.get(assessment_line_id, []))
                        relevant_score = average(relevant_assessment_line_dict.get(assessment_line_id, []))
                        #将结果写入数据库中
                        month_score = MonthScore.objects.filter(assessment_line__id = assessment_line_id,month_record=month_record,owner__id=user_id)
                        if month_score:
                            month_score = month_score[0]
                            month_score.done = True
                            if relevant_score:
                                score =float(self_score*self_weight+higher_score*higher_weight+relevant_score*relevant_weight)/(self_weight+higher_weight+relevant_weight)
                            else:
                                score = float( self_score * self_weight + higher_score * higher_weight + relevant_score * relevant_weight) / ( self_weight + higher_weight)
                            score = round(score,2)
                            all_percent += assessment_line_percent_dict.get(assessment_line_id,0)
                            total_score += score*assessment_line_percent_dict.get(assessment_line_id,0)
                            month_score.score = round(score,2)

                            month_score.save()
                month_record.score = round(float(total_score/all_percent),1)
                month_record.save()


    return HttpResponseRedirect('/performance/list/?detail=1')
