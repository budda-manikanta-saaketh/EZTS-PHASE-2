class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->",end="")
                temp = temp.next
            print("Null")
    def push(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            p=self.head.data
            self.head=self.head.next
            print("popped element:",p)
    def top(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            print("the Top Element is",self.head.data)
obj=Stack()
while True:
    n=int(input("1.push\n2.pop\n3.display\n4.top\n5.exit\nenter your choice:"))
    if n==1:
        num=int(input("enter the element:"))
        obj.push(num)
    elif n==2:
        obj.pop()
    elif n==3:
        obj.display()
    elif n==4:
        obj.top()
    else:
        break

