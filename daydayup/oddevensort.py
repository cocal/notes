# -*- coding: utf-8 -*-

# 基数偶数排序 要求把一列数的基数放前面 偶数放后面

## 快速排序变种应用

li = range(10)

def oddEvenSort(li):
    lenth = len(li) - 1
    i = -1  
    tag = li[lenth]
    for j in range(lenth - 1) : 
        if li[j]%2 != 0 :
            i += 1
            li[i],li[j] = li[j], li[i]
    li[i+1],li[lenth] = li[lenth], li[i+1]
    print li

oddEvenSort(li)