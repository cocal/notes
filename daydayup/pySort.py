# -*- coding: utf-8 -*-
#没时间了 写个冒泡排序好了  - -


li = [1,1,5,6,7,3,2,1,9,0]

def bubSort(li):
    lenth = len(li)
    for x in range(lenth-1,-1,-1) :
        print  x
        for i in range(x) :
            if li[i] < li[i+1] :
#                 print li[i],li[i+1]
                li[i] , li[i+1] = li[i+1] , li[i]
print li
bubSort(li)
print li

#python 在默认情况下居然有最大递归深度1000限制？ 
max_rec = 1000
def recursion(i):
    if i < 1001 :
        i = i + 1
        print i
        recursion(i)
    else :
        print 'ops ~ return' #默认情况下是不会输出这行的 ....
# recursion(1)
##当递归次数大于1000次 会抛出   
##File "C:\Users\cocal\git\notes\daydayup\pySort.py", line 25, in recursion
##    recursion(i)
##RuntimeError: maximum recursion depth exceeded

##查了下原因是 python为了防止无限循环递归 特地设置了限制。
##修改 递归次数限制为

##import sys
##sys.setrecursionlimit(1500) # set the maximum depth as 1500

##不过每次写程序使用到递归 需要考虑到最大递归次数是个好习惯

import sys
sys.setrecursionlimit(1100)
recursion(1)
#到1001次时就听推出循环了

