# -*- coding: utf-8 -*-

#实现一颗树

class Node():
    def __init__(self,left=None,right=None,val=0):
        self.left = left
        self.right = right
        self.val = val

class binarryTree():
    def __init__(self):
        self.root = Node()
   
    def insertNode(self,date): 
        print date     
        node = Node(val=date)
        r = self.root
        while r != None :
            p = r
            if r.left == None and r.right == None : 
                r = r.left
            elif r.left != None and r.right == None :
                r = r.right
            elif r.left.left == None or r.left.right == None:
                r = r.left
            else :
                r = r.right
        if p.left == None :
            p.left = node
        else :
            p.right = node
    
def showTheTree(node,deep = 0):
    if node == None :
        return
    print node.val,deep
    deep += 1
    showTheTree(node.left, deep)
    showTheTree(node.right,deep)


b = binarryTree()

for i in [1,2,3,4,5,7,8,6,4] :
    b.insertNode(i)   
showTheTree(b.root)     