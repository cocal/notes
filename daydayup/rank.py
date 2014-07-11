# -*- coding: utf-8 -*-

str = range(3)
from itertools import permutations
#for x  in permutations(str):
#    print x
#def rank(str):
#    
#rank(str)

#全排列  递归
def rank(l):
#    print '--',l  
    if(len(l)==1):  
        yield (l[0],)  
    for i in range(len(l)):
#        cur = l[i]  
#        del l[i]
#        print '--',l  
        s = l[:i] + l[i+1:]  
#        p=perm(s) 
#        print '--',p 
        for x in rank(s):
            yield (l[i],) + x
#            temp = []
#            temp.append(l[i]) 
#            r.append(temp.append[x])

#for x in perm(str):
#    print x
    
def rank2(l):
    if(len(l)<=1):
        return (l[0],)
    res = ()
    for i in range(len(l)):
        s = l[:i] + l[i+1:]
        for x in rank2(s):
            res = (l[i],) + x
    return res

print rank2(l=['1','2','3'])