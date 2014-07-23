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



#select算法 类似快速排序 将数列按照某个元素分堆 知道最小堆为k为止


# li = [1,5,6,3,2,7,8,9,0,4]


def partSelect(li,right,left):
#     lenth = len(li) - 1
    pivot = li[left]
    i = right - 1
    for j in range(right,left) :
        if li[j] < pivot :
            i += 1
            li[i] , li[j] = li[j],li[i]

    li[i+1],li[left] = pivot,li[i+1]
    return i+1
# partSelect(li, 0, len(li)- 1)
# print '--',li

def quickSelect(li,right,left,k):
    print 'q'
    print li
    if right >= left :
        return right
    flag = partSelect(li, right, left)
#     if flag == k + 1 :
#         return flag - 1
    print flag

    if flag - right > k - 1 :
        flag = quickSelect(li, right, flag - 1, k)
    elif flag - right < k - 1 :
        flag = quickSelect(li, flag + 1, left, k - 1)
    print li[:flag+1]   
    return  flag
li = [1,2,3,4,5,6,7,8,9]
li = [1,2,3,4,5,6,7,8,9,0,11,13,17,31,42,16,15]
print 'quickSelect:',li
quickSelect(li, 0,len(li)- 1 ,8)
print 'quickSelect:',li

# li = [1,2,3,4,5,6,7,8,9,0,11,13,17,31,42,16,15]

def quickSort(li,start,end):
    flag = li[end]
    i = start - 1
    for x in range(start,end) :
        if li[x] < flag :
           i += 1
           li[i],li[x] = li[x],li[i]
    li[i+1] , li[end] = li[end] ,li[i+1] 
    return i+1
# print quickSort(li, 0, len(li) - 1)
# print li


def quickSelect2(li,start,end,k):
    if start >= end :
        return start
    flag = quickSort(li, start, end)
    num = flag - start + 1
#     if num == k :
#         return flag
    if num > k : 
        flag = quickSelect2(li, start, flag-1, k)
    elif num < k : 
        flag = quickSelect2(li, flag + 1, end, k - num)
    
    return flag
li = [1,2,3,4,5,6,0]
print '------'
res = quickSelect2(li,0,len(li)-1, 6)
print res,li[:res+1]








