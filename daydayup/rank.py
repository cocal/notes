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
    res = []
    if(len(l)<=1):
        res.append((l[0],)) 
        print res
        return res
#     res = []
    for i in range(len(l)):
        s = l[:i] + l[i+1:]
        print 's',s
#         temp = ()
        for x in rank2(s):
            print 'x',x
            temp = (l[i],) + x
            print 'temp',temp
            res.append(temp)     
    return res

print 'res',rank2(l=['1','2','3'])

def test():
    return (1,)




















