# -*- coding: utf-8 -*-
#寻找和为定值的两个数

def sumOfNums(li,sum):
#     i = 0
    lenth = len(li) 
    for i in range(lenth - 1) :
        for j in range(i,lenth):
            if li[i] + li[j] == sum :
                print i,j,':',li[i],li[j]
                
li = [1,2,3,4,5,6,7,8,9]

sumOfNums(li, 15)       