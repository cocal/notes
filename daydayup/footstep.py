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
for i in range(10):
    print getSteps(i)