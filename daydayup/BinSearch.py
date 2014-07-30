# -*- coding: utf-8 -*- 

#python 实现二分查找

li = [1,2,3,4,5,6,7,8,9]


def binSearch(li,val):
    begin = 0
    
    end = len(li) - 1
    print  end
#     mid = lenth/2
    i = 0
    while begin < end : 
        
        mid = begin + (end - begin) / 2
        print '对半次数  : ', i , 'mid :', mid, 'li[mid] =',li[mid]
        if li[mid] > val :
            end = mid - 1
        elif li[mid] < val :
            begin = mid + 1
        else :
            print mid
            return mid
        i += 1
    if begin == end and li[end] == val:
        print li[end], end
        return end
    else :
        print 'err val'
        return 'err'
# binSearch(li, 7)
binSearch(li, 10)

