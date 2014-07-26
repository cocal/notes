# -*- coding: utf-8 -*-
#寻找和为定值的两个数
import pySort

def sumOfNums(li,sum):
#     i = 0
    lenth = len(li) 
    for i in range(lenth - 1) :
        for j in range(i,lenth):
            if li[i] + li[j] == sum :
                print i,j,':',li[i],li[j]
                
li = [1,2,3,4,5,6,7,8,9]

sumOfNums(li, 10) 

#上面那个方法的消耗是O(n^2)

def sumOfNums2(li,sum):
    lenth = len(li)
    pySort.quSort(li,0,lenth-1)
    j = lenth - 1
    i = 0
    while i < j    :
        desSum = li[i] + li[j]
        if desSum == sum :
            print i,j,':',li[i],li[j]
        if desSum > sum : 
            j -= 1
        else :
            i += 1 
        
print '2---'            
li = [1,2,3,4,5,6,7,8,9] 
sumOfNums2(li,10) #无序数组时 时间消耗为O(NlogN + N)