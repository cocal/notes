# -*- coding: utf-8 -*- 

#寻找和为定制的K个数

# li = [1,2,3,4,5,6,7,8,9]
lires = []
def sumOfKnums(sum,n):
    if n <= 0 or sum <= 0: 
        return
    if sum == n :
#         lires.append(n)
        print lires,n
        
    lires.append(n)
    sumOfKnums(sum - n, n - 1)
    lires.pop()
    sumOfKnums(sum, n - 1)
    
sumOfKnums(10, 6)


    
    
    