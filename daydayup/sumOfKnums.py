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
    
sumOfKnums(10, 1)



##寻找最大的几个数之和

li = [1,2,-3,4,-1,5,-7,10,1]

def maxSumsOfnums(li):
    lenth = len(li)
    maxSum = 0
    currSum = 0
    for i in range(lenth) :
        for j in range(i,lenth) :
            for k in range(i,j) :
#                 print k,
                currSum += li[k]
#             print
            if maxSum < currSum :
                 maxSum = currSum
            currSum = 0
        
    return maxSum

print maxSumsOfnums(li)
print 
    
    
##方法二 
li = [1,2,-3,4,-1,5,-7,10,1]
def MaxSub(li):
    currSum = 0
    maxSum = 0
    for x in li :
        if x > x + currSum :
            currSum = x
        else :
            currSum = currSum + x 
        if maxSum < currSum :
            print maxSum
            maxSum = currSum
    return maxSum

print MaxSub(li)
        
    
    
    
    
    

    
    
    