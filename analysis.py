# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:07:28 2017

@author: Crystal
"""
import datetime
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

def interval(date1,date2):
#    year,month,day
#    hour,minute,second

    trans1=str2date(date1)
    trans2=str2date(date2)
    
    dateInter=(datetime.datetime(trans2[0],trans2[1],trans2[2],trans2[3],trans2[4],trans2[5])-datetime.datetime(trans1[0],trans1[1],trans1[2],trans1[3],trans1[4],trans1[5])).seconds
    if dateInter>80000:
        dateInter=86400-dateInter
    return dateInter
    
def str2date(date):
    s=date.split(' ')
    year=int(s[0].split('/')[0])
    month=int(s[0].split('/')[1])
    day=int(s[0].split('/')[2])
    
    hour=int(s[1].split(':')[0])
    minute=int(s[1].split(':')[1])
    second=int(s[1].split(':')[2])
    
    l=[year,month,day,hour,minute,second]
    return l

def calInter(fileName):
    df=pd.read_csv(fileName,encoding='gbk')
#    print df['date']
    pre=df['date'][0]
    inter=[]
#    for i in list(df['date'].index):
#        print df['date'][i]
    for i,row in df['date'].iteritems():
        if i==0:
            continue
        nex=row
        inter.append(interval(pre,nex))
        pre=nex
    inter.append('')
    df['interval']=inter
    df.to_csv(fileName,encoding='gbk',index=False)

   

def blockAnalysis(fileName):
    df=pd.read_csv(fileName,encoding='gbk')
    interval=df['interval']
    print '---------------区块相关--------------------'
    print '最大值：',interval.max(),'最小值：',interval.min(),'平均值:',interval.mean(),'方差：',interval.var()
    
def forkAnalysis(fileName):
    df=pd.read_csv(fileName,encoding='gbk')
    block=df['block']
    result=[]
#    print block
    for i,row in block.iteritems():
        if '已孤儿' in row.encode('utf-8'):
            result.append(int(row[:-5].encode('utf-8')))
        
            
    pre=result[0]
    for i in xrange(1,len(result)):
        temp=result[i]
        result[i]=result[i]-pre
        pre=temp
    ser=Series(result)
    print '---------------分叉相关--------------------'
    print '最大值：',ser.max(),'最小值：',ser.min(),'平均值:',ser.mean(),'方差：',ser.var()
        
        
        
    
if __name__=='__main__':
#    print interval('2009/1/10  23:57:02','2009/1/10  23:57:58')
#    calInter('output.csv')
#    analysis('test.csv')
#    s1='sssaddd(已孤儿)'
#    s2='wen'
#    print s1.find('已孤儿')
#    result=[]
#    if '已孤儿' in s1:
#        result.append(s1[:-11])
#    print result
    blockAnalysis('output2.csv')
    forkAnalysis('output2.csv')
