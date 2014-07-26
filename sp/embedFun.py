# -*- coding: utf-8 -*-
'''
Created on 2014年7月26日

@author: cocal
'''

## 今天看代码的时候 发现python支持函数内嵌函数  o.o
def testA():
    print 'this is A'
    def testB():
        print 'testB is running'
    testB()

if __name__ == '__main__' :
    testA()
