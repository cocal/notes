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
# showTheTree(b.root)     


### 二叉查找树

class BinaryTree(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def instert(self,val):
        if val < self.val :
            if self.left != None :
                self.left.instert(val)
            else :
                node = BinaryTree(val)
                self.left = node
        else :
            if self.right != None :
                self.right.instert(val)
            else :
                node = BinaryTree(val)
                self.right = node
    def findNode(self,val):
        if self.val == val :
            return val
        if self.val > val : 
            return self.right.findNode(val)
        else :
            return self.left.findNode(val)
        
    def delNode(self,val):
        currNode = self 
        parent = self
        while val < currNode.val :
            parent = currNode 
            if currNode < val :
                currNode = currNode.left
            else :
                currNode = currNode.right
        
        if currNode.left == None and currNode.right == None :
            if parent.left.val == currNode.val :
                parent.left == None
            else :
                parent.right == None
        elif currNode.left != None and currNode.right == None :
            if parent.left.val == currNode.val :
                parent.left == currNode.left
            else :
                parent.right == currNode.left
        elif currNode.left == None and currNode.right != None :
            if parent.left.val == currNode.val :
                parent.left == currNode.right
            else :
                parent.right == currNode.right
        else :
            temp = currNode.right
            temp = self._getMinNodeForDel(temp)
            currNode.val = temp.val   
    def _getMinNodeForDel(self,node):
        parentNode = node
        currNode = node
        while currNode.left != None :
            parentNode = self
            currNode = currNode.left
#         if currNode.right != None :
        parentNode.left = currNode.right
        currNode.right = None
        return currNode 
            

bTree = BinaryTree(6)

for i in range(10) :
    bTree.instert(i)
showTheTree(bTree,0)
bTree.delNode(7)
print '---'
showTheTree(bTree,0)
