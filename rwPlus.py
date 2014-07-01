# -*- coding: utf-8 -*-
'''
Created on 2014年6月30日

@author: cocal
'''

import re


def plus(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mul(a=0,b=0):
    return a*b

def div(a=0,b=1):
    if b == 0:
        return a
    else:
        return a/float(b)

opterator = {'+':plus,'-':sub,'*':mul,'/': div}
initOptval = {'+':0,'-':0,'*':1,'/':1}
def optMath(val1,val2,opt):
    return opterator.get(opt)(val1,val2)
    
##前缀表达式
def testplus(str):
    r1 = re.compile('[0-9]+') #判断是否为数字
    r2 = re.compile('[\+\*/\-]') #判断是否为属性符号
    str1 = []; #操作符队列
    str2 = []; #数值队列
    currentOpt = '='
    currentVal = 0
    for x in range(len(str)):
        temp = str[x]
        if temp == '(' :
#             print  currentVal
            str2.append(currentVal)
            currentVal = 0
        elif r2.match(temp) :
            str1.append(temp)
            currentOpt = temp
            currentVal = initOptval.get(temp)
        elif r1.match(temp):
            currentVal = optMath(currentVal,int(temp),currentOpt)
#             currentVal = currentVal + int(temp)
        elif temp == ')' :
            str1.pop()
            if len(str1) == 0:
                print 'result is %d',currentVal 
            else :
                currentVal = optMath(currentVal,str2.pop(),str1[-1])
#             currentVal = str2.pop() + currentVal      
            
            
#     print str1
#     print str2


if __name__ == '__main__':
    testplus('(/ 4 2)')
#     testplus('( + 1 9 8 (* 1 2 3) ( / 2 3 ))')
#     print 4/float(8)
    print 'done'