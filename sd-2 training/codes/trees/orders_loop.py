class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    current=root
    stack=[]
    done=0
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print (current.val),
            current=current.right
        else : 
            break
    print()
#input
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
root.left.right=Node(5)
inorder(root)