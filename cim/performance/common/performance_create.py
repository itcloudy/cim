#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/24

@author: cloudy
@description:
'''
from ..models import AssessmentLine,Record,MonthScore

def create_record(department_assessments,mark,owner,start_date,month_record,wait_higher,wait_self):
    '''生成待打分记录'''
    if not department_assessments or not mark or not  owner or not start_date:
        return  False

    bulk_list = []
    for department_assessment in department_assessments:

        # 查找相关考核项
        assessment_lines = AssessmentLine.objects.filter(assessment__id=department_assessment.id)
        for assessment_line in assessment_lines:

            bulk_list.append(Record(
                assessment_line=assessment_line,
                owner=owner,
                mark=mark,
                date_time=start_date,
                month_record =month_record,
                wait_higher=wait_higher,
                wait_self=wait_self))
    if bulk_list:
        return Record.objects.bulk_create(bulk_list)
    return  False

def create_month_score_record(department_assessments,month_record,owner):
    '''生成阅读考核结果记录'''
    if not department_assessments or not month_record or not  owner :
        return False
    bulk_list = []
    for department_assessment in department_assessments:
        # 查找相关考核项
        assessment_lines = AssessmentLine.objects.filter(assessment__id=department_assessment.id)
        for assessment_line in assessment_lines:
            bulk_list.append(MonthScore(
                month_record = month_record,
                owner = owner,
                assessment_line = assessment_line,
                done =False,
            ))
    if bulk_list:
        return MonthScore.objects.bulk_create(bulk_list)
    return  False
