# -*- coding: utf-8 -*-
'''
Created on 2014年7月6日

@author: cocal
'''
#以下内容参考自 http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
#生成器 
#搜罗网上一大堆内容 发现讲生成器和迭代器大都讲得很浅显。生成器这么NB的功能怎么能这么被忽略掉呢。

#首先带有yield关键词的函数称之为生成器generator
#网上一般的例子为：
def fib(max):  
    a, b = 0, 1            
    while a < max:  
        yield a            
        a, b = b, a + b  

for x in fib(5):
    print x,
#这样简单的几行就实现了一个Fibonacci（斐波那契）数列。 
#这样有和普通的函数有什么区别 这样有什么优势 
print

#普通青年实现的斐波那契数列为
def fibCommon(max):
    a = 0
    b = 1
    c = 0
    while c < max:
        print a,
        b = a + b
        a = b - a
        #python可以这么写 a , b = b , a + b
        c = c + 1
print 'common ------'
fibCommon(5)

#这样问题就出来了 我们调用这个函数就直接打印出来了
#如果要直接获得这个数列怎么办， 有办法的
def fibCommon2(max):
    a, b, c = 0, 1, 0
    l = []
    while c < max:
        l.append(a)
        a, b = b, a + b

print fibCommon2(5)
