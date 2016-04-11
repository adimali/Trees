#!/usr/bin/python
from random import randint
from drawtree import draw_level_order # print_tree requires this
class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        

class Tree:
    def __init__(self):
        self.root = None
        self.size =0

    def insert(self, key, val):
        self.size +=1
        if(self.root == None):
            self.root = Node(key,val)
        else:
            self._add(key, val, self.root)

    def _add(self, key, val, node):
        if(key < node.key):
            if(node.left == None):
                node.left=Node(key,val,parent=node)                
            else:
                self._add(key, val,node.left)
        else: # if key is equal to node.key then it goes in right sub tree
            if (node.right==None):
                node.right=Node(key, val,parent=node)
            else:
                self._add(key, val, node.right)

    def minimum(self):
        if self.root==None:
            return "empty tree"
        else:
            return self._min(self.root).key
    def _min(self, node):
        if node.left==None:
            return node
        else:
            return self._min(node.left)
    def maximum(self):
        if self.root==None:
            return "empty tree"
        else:
            return self._max(self.root).key
    def _max(self, node):
        if node.right==None:
            return node
        else:
            return self._max(node.right)    

    def search(self,key):
        if self.root==None:
            return "empty tree"
        else:
            Nd=self._search(key,self.root)
            if Nd:
                return Nd.val
            else:
                return "Key not found"
        
    def _search(self,key, node):
        if key==node.key:
            return node
        elif key>node.key:
            if node.right==None:
                return None
            else:
                return self._search(key,node.right)
        else:
            if node.left==None:
                return None
            else:
                return self._search(key,node.left)

    def _successor(self,node):
        return self._min(node.right)
            
        
    def delete(self,key):
        if self.root==None:
            return "empty tree"
        else:
            Nd=self._search(key, self.root)
            if Nd:
                self._delete(Nd)
                self.size-=1
                return "Key : " + str(key) + ", successfully deleted"
            else:
                return "Key not found"
    def _delete(self,node):
        if node.right == None and node.left == None:
            if node==self.root:
                self.root=None
            elif node==node.parent.left:
                node.parent.left=None
            else:
                node.parent.right=None
        elif node.right==None:
            if node==self.root:
                self.root=node.left
                node.left.parent=None
            elif node==node.parent.left:
                node.left.parent=node.parent
                node.parent.left=node.left
            else:
                node.left.parent=node.parent
                node.parent.right=node.left
        elif node.left==None:
            if node==self.root:
                self.root=node.right
                node.right.parent=None                
            elif node==node.parent.left:
                node.parent.left=node.right
                node.right.prent=node.parent
            else:
                node.parent.right=node.right
                node.right.parent=node.parent
        else:# Both children are present, now we have to replace the 
                    #node by its successor in the right subtree
            S=self._successor(node)
            if S.right:
                S.right.parent=S.parent
                if S.parent.left==S:
                    S.parent.left=S.right
                else:
                    S.parent.right=S.right
            else:
                if S.parent.left==S:
                    S.parent.left=None
                else:
                    S.parent.right=None
            if node==self.root:
                S.parent=None
                self.root=S
            else:
                S.parent=node.parent
                if node==node.parent.left:
                    node.parent.left=S
                else:
                    node.parent.right=S
                
            S.left=node.left
            S.right=node.right
            

    def in_order(self):
        for n in self._in_order(self.root):
            yield n.key

    def _in_order(self,node):
        if node!=None:
            for n in self._in_order(node.left):
                yield n
            yield node
            for n in self._in_order(node.right):
                yield n
    def pre_order(self):
        for n in self._pre_order(self.root):
            yield n.key

    def _pre_order(self,node):
        if node!=None:
            yield node
            for n in self._pre_order(node.left):
                yield n
            for n in self._pre_order(node.right):
                yield n

    def post_order(self):
        for n in self._post_order(self.root):
            yield n.key

    def _post_order(self,node):
        if node!=None:
            for n in self._post_order(node.left):
                yield n            
            for n in self._post_order(node.right):
                yield n            
            yield node
            
    def level_order(self):
        q=[]
        q.append(self.root)
        while len(q)!=0:
            n=q.pop(0)
            yield n.key
            if (n.left!=None):
                q.append(n.left)
            if (n.right!=None):
                q.append(n.right)
                
           
    def print_tree(self):
        q=[]
        r='{'
        q.append(self.root)
        while len([i for i in q if type(i)!=str])!=0:
            n=q.pop(0)
            if n=="#":
                r+=n+','
            else:
                r+=str(n.key)+','
            if (n!="#"):                  
                if (n.left!=None):
                    q.append(n.left)
                else:
                    q.append("#")
                if (n.right!=None):
                    q.append(n.right)
                else:
                    q.append("#")
        draw_level_order( r[:-1]+'}')

    def height(self):
        return self._height(self.root)
    def _height(self, node):
        if node is None:
            return 0
        else:
            return max(self._height(node.left),self._height(node.right))+1

# Example use

tree = Tree()
Key=[]
Value=[]
for i in range(15):
    Key.append(randint(0,9))
    Value.append(randint(0,90))
    tree.insert(Key[i],Value[i])
    print Key[i], Value[i]


tree.print_tree()
print "minimum = " , tree.minimum()
print "maximum = " , tree.maximum()
print "Value in ", Key[4], " = ", tree.search(Key[4])
print "Tree Size = ",tree.size
print "Height= ",tree.height()
print "in_order traversal = "  ,[i for i in tree.in_order()]
print "pre_order traversal = "  ,[i for i in tree.pre_order()]
print "post_order traversal = "  ,[i for i in tree.post_order()]
print "level_order traversal = "  ,[i for i in tree.level_order()]
print tree.delete(Key[0])
tree.print_tree()

