class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key
def insert(root,key):
        if root is None : 
            return  Node(key)
        else:
            if root.val==key:
                return root
            elif root.val<key:
                root.right=insert(root.right,key)
            else:
                 root.left=insert(root.left,key)
        return root
def search(root,key):
     if root is None:
          return False
     if  root.val ==key:
          return root
     if root.val<key:
          return search(root.right,key)

     return search(root.left,key)
#inorder tranversal
def InOrder(root):
     if root:
          InOrder(root.left)
          print(root.val)
          InOrder(root.right)
n=Node(50)
n=insert(n,30)
n=insert(n,20)
n=insert(n,40)
n=insert(n,70)
n=insert(n,60)
n=insert(n,80)
num=int(input("enter the number to search:"))
r=search(n,num)
if r is False:
     print("Not found")
else:
    print(r.val,"is found")