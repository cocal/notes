# -*- coding: utf-8 -*-
'''
Created on 2014年7月12日

@author: cocal
'''
##判断字符串是否属于回文

str = '321abcdsdcba123'

def isPalindrome(str):
    i = len(str)
    print i,i/2
    j = i
    for x in range(i/2):
        j = j -1
        if str[x] == str[j] :            
            continue
        else:
            return False
    return True

print isPalindrome(str)


#其实还有更简单的方法
def isPalindrome2(str):
    return str == str[::-1]

print isPalindrome2(str)

##找出字符串中最长回文

def LongestPalindrome(str):
    l = len(str)
    max = 0
    for i in range(l) :
        k = 0
        while (i-k > 0) and (i + k < l) : #只考虑奇数情况
            if str [i-k] != str[i+k] :
#                 print i,str[i-k],str[i+k] 
                k = k -1
                break
            else :
                k = k + 1

        if max < k * 2 + 1:
            max = k * 2 + 1
            print i
            print str[i-k:i+k+1]
    print max

LongestPalindrome('sdscabdbaccc')
