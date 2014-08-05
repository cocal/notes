# -*- coding: utf-8 -*-

#跳台阶问题 有n阶台阶。现在可以一次跳一个 或者 一次跳两格 问有几种办法


def getSteps(n):
    if n == 1 : 
        return 1
    currentSteps = 1
    lastSteps = 1
    res = 0
    for i in range(2,n+1) : 
        res = currentSteps + lastSteps
        lastSteps, currentSteps = currentSteps, res
    return res
# for i in range(10):
#     print getSteps(i)
    
    
##荷兰三色国旗问题 
##现有一串由1，2，3组成的乱序数列 [1,2,3,3,2,1,1,2,3,3,2,2] 要求按[1,1,1,2,2,2,3,3]格式排列

##也是一个快排的变种
li = [1,2,3,3,2,1,1,2,3,3,2,2]
def threeBolls(li):
    print li
    lenth = len(li) - 1
    begin = 0
    current = 0
    end = lenth
    while current < end :
#         print li,current
        if li[current] == 1 : 
            li[begin], li[current] = li[current], li[begin]
            begin += 1
            current += 1
        elif li[current] == 2 :
            current +=1
            continue
        elif li[current] == 3 :
            li[current],li[end] = li[end],li[current]
            end -= 1
    print li 
    
threeBolls(li);




