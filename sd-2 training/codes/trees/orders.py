class Node:
    def __init__ (self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        print(root.val, end = " ")
        printPreorder(root.left)
        printPreorder(root.right)
        
n=Node(100)
n.left=Node(400)
n.right=Node(500)
n.left.left=Node(700)
n.left.right=Node(600)
n.left.right.left=Node(900)
n.right.left=Node(800)
n.right.right=Node(200)
n.right.right.left=Node(300)
print("InOrder traversal of the tree is:",end=" ")
printInorder(n)
print("\nPostorder traversal of the tree is:",end=" ")
printPostorder(n)
print("\nPreorder traversal of the tree is",end=" ")
printPreorder(n)