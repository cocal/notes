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
    print 'q',li,li[right:left+1],'r=',right,'l=',left,k
    if right >= left :
        return right
    flag = partSelect(li, right, left)
#     if flag == k + 1 :
#         return flag - 1
    print flag,li[flag]
    print 's',li
    if flag - right > k - 1 :
        flag = quickSelect(li, right, flag - 1, k)
    elif flag - right < k - 1 :
        flag = quickSelect(li, flag + 1, left, k - right)
    print li[:flag+1]   
    return  flag
li = [1,2,3,4,5,6,7,8,9]
li = [1,2,3,4,5,6,7,8,9,0,11,13,17,31,42,16,15]

li = [1,11,2,12,3,13,4,14,5,15,6,16,7,17]
print 'quickSelect:',li
quickSelect(li, 0,len(li)- 1 ,8)
print 'quickSelect:',li














