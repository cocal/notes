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
dict2.get(1)()

def saidStr(tosb,str):
    print 'said to', tosb , ':' , str
dict3 = {'said':saidStr} #字典使用带参数的函数 - -.... 目测应存的是函数指针

dict3.get('said')('sb','you are')



class M:
    i = 1
    def __init__(self):
        self.i = 2
        print 'new M'
    
def getM():
    m = M();
    return m;


dict4 = {1: getM()} #字典中直接调用方法....害我纠结了半天

print dict4.get(1).i


##其余的方法就很简单了
dict5 = dict(val1= '1', val2 = '2', val3 = '3')
print dict5

for x in dict5.keys():
    print 'key :', x
    print 'val :',dict5.get(x)







