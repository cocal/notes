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


def foo(m):
    k = 0
    print 'm =',m,'k =',k
    def bar():
        n = 3 
#         m += 1 #但是不能给改变外部函数的值 使用这行编译器会抛出异常
        print 'm + n = ',m,'+',n,'=',m+n #内部函数可以直接调用外部函数的变量
        
    bar()


#如果返回一个函数呢
def foo2(m,n):
    print 'm',m
    def bar2(n):
        n += 1
        return m + n
#     return bar2(n)
    return bar2
if __name__ == '__main__' :
    testA()
    foo(6)
    
    x = foo2(1, 2)
    print 'x : ',x(3) #神奇的调用 不过这样调用会很容易出问题吧
    
    