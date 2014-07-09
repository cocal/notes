# -*- coding: utf-8 -*-
'''
Created on 2014年7月7日

@author: cocal
'''
##八皇后问题
## 八皇后问题 题目： 在一个8×8宫格的国际棋盘上，放8个皇后使得任意一个皇后都不能吃掉其他的皇后（即 任意两个皇后不能在同一列、同一行、同斜线上)
##这里先考虑8宫格情况下。

##普通青年解法
#摔根本不会做嘛～
#我们可以用一个数组来表示每列的皇后 [0,1,2,3,4,5,6,7]这样每个皇后就都不在同一列同一行了 现在只需要判断每个棋子不在同一斜线上就好了
#传入val1与list的值是否在一条斜线上 
# def isBias(valList,dot):
#     dot_y = len(valList)
#     y = 0
#     for x in valList:
#         if (x - dot)/(y - dot_y) == 1:
#             return True
#         else:
#             y = y + 1
#     return False     
# 
# print 'test : ', isBias([0,2], 4)
#
 
from itertools import permutations
n = 4
valList = range(n)
for vec in permutations(valList):#将valList生成排列
    if (n == len(set(vec[i] + i for i in valList))
          == len(set(vec[i] - i for i in valList))): ##终于想明白了...
        print vec

#明天继续吧 - -....     

print '----yield'
#参考《Python基础教程》  先这样吧       
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False
     
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,)+result
                    
for line in list(queens(8)):
    print line

##自己实现的八皇后丑死了..
def isDagonal(dots,nextX):
    l = len(dots)
    i = -1
    for x  in dots:
        i = i + 1
        if x + l - i == nextX or x - l + i == nextX or x == nextX:
#            print 'No vil -- ' ,dots,'nextX : ',nextX
            return True
        else:
            continue
#    print 'Done --',dots,'nextX : ',nextX
    return False

#isDagonal([0,2], 4)

def queen(n=4,qu=[]):
#    print '-----递归--------'
    if len(qu) == n:
        return True
    for pos in range(n):
        if isDagonal(qu,pos):
            continue
        else:
            qu.append(pos)
            if queen(n,qu) :
                print '-----------',qu
#                yield qu
                qu.pop()
            else :
               qu.pop()
                
#    print '------递归结束-----'
    return False
    
queen(8)


        
    