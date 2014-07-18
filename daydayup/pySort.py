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