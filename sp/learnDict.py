# -*- coding: utf-8 -*-
'''
Created on 2014年7月3日

@author: cocal
'''
## 这几天用到了python的字典类型 觉得蛮有趣的 

dict1 = {1:'this is a test'}
print dict1.get(1)

def saidHi():
    print 'hi'

dict2 = {1:saidHi} #字典里存放函数 
dict2.get(1)

def saidStr(tosb,str):
    print 'said to', tosb , ':' , str
dict3 = {'said':saidStr} #字典使用带参数的函数 - -....

dict3.get('said')('sb','you are')

















