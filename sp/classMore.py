# -*- coding: utf-8 -*-
'''
Created on 2014年7月5日

@author: cocal
'''
##昨天被教育说python的高级用法 今天特意拉出来看了下....

#魔法方法 -- 
class Magic():
    val2 = 'ko'
#     def __init__(self):
#         print 'init.....'
    def __init__(self,val=0):
        print 'init......2'
        self.val = val
        
    ##__str__是个个神奇的方法     当程序员需要对类进行说明可以使用此方法
    #此方法必须要return一个str。
    #当有此方法时 可以直接print 这个对象。
    def __str__(self):
        return '这是一个描述类的方法 : val2 的值为 ： ' + self.val2  
    
    
    
 #迭代器 
 #理解了迭代器对程序运行有一定帮助 网上看到的一个迭代器例子
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration #抛出这个异常后 for循环会停止
        self.index = self.index - 1 #擦坑爹呢 这个居然是倒序输出
        return self.data[self.index]


#生成器 
#原谅我脑壳有个包 还是不太透彻的理解生生成器 下面就依葫芦画瓢试试
        
    
if __name__ == '__main__' :      
    m = Magic()
    print m.val
    print m  # #打印出类的描述
    r = Reverse('12334567')
    for x in r:
        print x
