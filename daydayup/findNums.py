# -*- coding: utf-8 -*-

##寻找最小的k个数
import pySort

li = [1,5,6,3,2,7,8,9,0]

#先排序 求出个数
def quickSelect(li,k=1):
    pySort.quSort(li,0,len(li) -1)
    print li[0:k+1]
    
# quickSelect(li, 8)

#维持k个元素 
def getKMax(li):
    max = 0
    for x in li:
        if x > max :
            max = x
    return max

def swapSelect(li,k=1):
    temp = li[0:k]
    max = getKMax(temp)
    for x in li[k:] :
        if max > x :
            temp.remove(max)
            temp.append(x)
            max = getKMax(temp)
    print temp
    print li
swapSelect(li, 5)
    
