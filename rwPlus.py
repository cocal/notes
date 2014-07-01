# -*- coding: utf-8 -*-
'''
Created on 2014年6月30日

@author: cocal
'''

import re

##前缀表达式
def testplus(str):
    r1 = re.compile('[0-9]+') #判断是否为数字
    r2 = re.compile('(\+|\*)') #判断是否为属性符号
    str1 = []; #操作符队列
    str2 = []; #数值队列
    currentOpt = '='
    currentVal = 0
    for x in range(len(str)):
        temp = str[x]
        if temp == '(' :
            str2.append(currentVal)
            currentVal = 0
        elif r2.match(temp) :
            str1.append(temp)
            currentOpt = temp
        elif r1.match(temp):
            currentVal = currentVal + int(temp)
        elif temp == ')' :
            currentVal = str2.pop() + currentVal
            str1.pop()
            print 'result is %d',currentVal 
            
    print str1
    print str2


if __name__ == '__main__':
    testplus('( + 1 9 8 (+ 1 2 3) ( + 2 3 ))')
    print 'done'