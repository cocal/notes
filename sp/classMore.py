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
    
if __name__ == '__main__' :      
    m = Magic()
    print m.val
    print m  # #打印出类的描述
