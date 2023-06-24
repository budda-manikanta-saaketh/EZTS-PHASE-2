class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            n.next=self.head
            self.head.prev=n
            self.head=n
    def insert_at_end(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=n
            n.prev=temp
    def insert_at_mid(self,loc,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            temp=self.head
            while temp.data!=loc:
                temp=temp.next
            n.next=temp.next
            temp.next.prev=n
            n.prev=temp
            temp.next=n
    def delete(self,loc):
        if self.head is None:
            print("List Empty")
        elif self.head.data==loc:
            self.head.next.prev=None
            self.head=self.head.next
        else:
            temp=self.head
            while temp.next.data!=loc:
                temp=temp.next
            if temp.next.next is None:
                temp.next=None
            else:
                temp.next.next.prev=temp
                temp.next=temp.next.next
    def display(self):
        n=int(input("\n1.Forward\n2.Backward\nEnter the choice:"))
        if n==1:
            p=self.head
            while p:
                print(p.data,"<->",end=" ")
                p=p.next
            print("NULL")
        if n==2:
            p=self.head
            while p.next is not None:
                p=p.next
            while p:
                print(p.data,"<->",end=" ")
                p=p.prev
            print("NULL")
obj = DoubleLinkedList()
while True:
    n = int(input("\n1.Create\n2.Insert at beginning\n3.insert at mid\n4.insert at end\n5.Display\n6.Delete\n7.Exit\nEnter a option:"))
    if n == 1:
        a = int(input("Enter the head value: "))
        n1 = Node(a)
        obj.head = n1
    elif n == 2:
        b = int(input("Enter a element: "))
        obj.insert_at_beg(b)
    elif n==3:
        a=int(input("Enter the element after which you want to enter:"))
        b=int(input("Enter a element:"))
        obj.insert_at_mid(a,b)
    elif n==4:
        b=int(input("Enter a element:"))
        obj.insert_at_end(b)
    elif n == 5:
        obj.display()
    elif n == 6:
        c = int(input("Enter the element you want to delete from the linked list: "))
        obj.delete(c)
    else:
        break

