# -*- coding: utf-8 -*-
'''
Created on 2014年6月30日

@author: cocal
'''

import re

##前缀表达式
def testplus(str):
    r1 = re.compile('[0-9]+')
    str1 = []; #操作符队列
    str2 = []; #数值队列
    for x in range(len(str)):
        if str[x] == '(' :
            pass
        elif str[x] == '+' :
            str1.append(str[x])
        elif r1.match(str[x]):
            str2.append(int(str[x]))
            
    print str1
    print str2


if __name__ == '__main__':
    
    testplus('( + 1 9 )')
    print 'done'