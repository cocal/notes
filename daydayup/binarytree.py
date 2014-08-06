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
        node = Node(val=date)
        
        r = self.root
        while r != None :
            p = r
            if r.left > node.val : 
                r = r.left
            else :
                r = r.right
        if p.val > node.val :
            p.left = node
        else :
            p.right = node
    
def showTheTree(node):
    if node == None :
        return
    print node.val
    showTheTree(node.left)
    showTheTree(node.right)


b = binarryTree()

for i in [1,2,3,4,7,8,6,4] :
    b.insertNode(i)   
showTheTree(b.root)     