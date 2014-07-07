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
    a, b, c = 0, 1, 0            
    while c < max:  
        yield a            
        a, b = b, a + b 
        c = c + 1 

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
print
 
#这样问题就出来了 我们调用这个函数就直接打印出来了
#如果要直接获得这个数列怎么办， 有办法的
def fibCommon2(max):
    a, b, c = 0, 1, 0
    l = []
    while c < max:
        l.append(a)
        a, b = b, a + b
        c = c + 1
    return l
print '-----common2'
print fibCommon2(5)

#如果这么写 肯定会被杨神鄙视了，“你懂不懂内存是很珍贵的！你知不知道 我们现在大数据用你这个方法轻松就把服务器跑挂了。重新改！”

#得 那么我们就用最新的牛逼哄哄的迭代器呗

class fibIte:
    def __init__(self,maxVal):
        self.a = 0
        self.b = 1
        self.c = 0
        self.max = maxVal
    def __iter__(self):
        return self    
    def next(self):
        if self.c < self.max:
            res = self.a
            self.a, self.b = self.b, self.a + self.b
            self.c = self.c + 1
            return res
        raise StopIteration()

print '----iterator '
for x in fibIte(5):
    print x,
print

##废了九牛二虎之力 弄出来给 杨神一看 “唉 看你也写不出来，看我写给你看” 说完手一抖 直接二进制编码就生成了。
#杨神放话了 不服来跑分...
# 生成器 二逼青年版版
def fibGen(max):  
    a, b, c = 0, 1, 0            
    while c < max:  
        yield a #带有 yield关键字的函数 会被解释成一个生成器 返回一个迭代对象。    
        a, b = b, a + b 
        c = c + 1 
print '-----generator'
for x in fibGen(5):
    print x,
print
print '----test'
#巧妙的是还可以这么用
g= fibGen(5);
print g.next()
print g.next()

#每次生成器都会生成不同的实例
x = fibGen(3)
y = fibGen(6)
for i in range(1,4,1):
    print 'x:',x.next()
    print 'y:',y.next(),y.next()

print    
#迭代器中如果有return 则抛出StopIteration终止迭代
def fibGen2(max):  
    a, b, c = 0, 1, 0           
    while c < max:  
        yield a #带有 yield关键字的函数 会被解释成一个生成器 返回一个迭代对象。    
        a, b = b, a + b 
        c = c + 1
        if c >= 5:
            return
print '-----generator2'
for x in fibGen2(10):
    print x,
    
##.....今天程序死循环居然把电脑跑挂了..看来python开销略大啊  查查资料看看
## 有个函数可以判断是否是生成器 isgeneratorfunction ...python 太扯了 = =
