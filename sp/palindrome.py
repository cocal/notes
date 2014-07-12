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

