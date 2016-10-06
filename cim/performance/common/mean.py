#!/usr/bin/env python
#coding=utf8
'''
Created on 2016/9/30

@author: cloudy
@description:
'''
import  math
def average(data_list=[]):
    '''求平均值'''
    list_len = len(data_list)
    if list_len==0:
        return 0
    total = 0
    for line in data_list:
        total += line
    return float(total)/list_len

def mean(data_list=[]):
    list_len = len(data_list)
    if list_len == 0:
        return 0
    total = 0
    for line in data_list:
        total += line*line
    return math.sqrt(total/list_len)
