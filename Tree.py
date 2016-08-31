# Write a function buildTree that returns a tree using the nodes and references implementation 

class BinaryTree(object):
    def __init__(self,rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None


#inset left
    def insertLeftChild(self,node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t


    def insertRightChild(self,node):
        if  self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rigthChild = self.rightChild
            self.rightChild = t


#     get leftchild
    def getLeftChild(self):
        return self.leftChild

#     get right child
    def getRightChild(self):
        return self.rightChild

#     root value
    def setRootValue(self,obj):
        self.key = obj

#     get root
    def getRootVal(self):
        return self.key



r = BinaryTree('a')
r.insertLeftChild('b')
r.insertLeftChild('d')
print(r.getLeftChild().getRootVal())
r.insertRightChild('c')
r.insertRightChild('e')
r.insertRightChild('f')
print(r.getRightChild().getRootVal())
