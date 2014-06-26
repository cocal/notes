# -*- coding: utf-8 -*-
'''
Created on 2014年6月26日

@author: cocal
'''
#搞笑方式实现前缀表达式 加法 
#1.下一步实现嵌套加法(+ 2 3 (+ 3 8))
def cal(str):
    print str
    str = str.replace('(', '')
    str = str.replace(')', '')
    val = str.split(' ')
#     print val
    res = 0    
    for v in val[1:]:
        res = res + int(v)     
#     res = int(val[1]) + int(val[2])
    print 'res is ' 
    print res
if __name__ == '__main__' :
    str = '(+ 2 3 8)'
    cal(str)
    print 'hehe'