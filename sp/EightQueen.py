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
n = 8
valList = range(n)
for vec in permutations(valList):#将valList生成排列
    if (n == len(set(vec[i] + i for i in valList))
          == len(set(vec[i] - i for i in valList))):
        print vec

#明天继续吧 - -....            
    