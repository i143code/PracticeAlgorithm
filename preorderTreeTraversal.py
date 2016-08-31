# preorder tree traversals
# concept: In a preorder traversal, visit the root node first, 
# then recursively do a preorder traversal of the left subtree,and follwed by the right subtree


#  Given
# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.data (the value of the node)
# """
def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)
