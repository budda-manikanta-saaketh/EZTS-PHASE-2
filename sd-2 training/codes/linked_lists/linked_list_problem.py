class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->",end="")
                temp = temp.next
            print("Null")
    def insert_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node
    def insert_at_mid(self,number,data):
        new_node=Node(data)
        if self.head is None:
            print("Linked List is empty")
        elif self.head.data==number:
            new_node.next=self.head.next
            self.head.next=new_node
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == number:
                    temp.next=new_node.next
                    temp.next=new_node
                    break
                temp = temp.next
    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, number):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.data == number:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == number:
                    temp.next = temp.next.next
                    break
                temp = temp.next
    def compare(self):
        temp=self.head
        li=[]
        while temp:
            li.append(temp.data)
        return li
obj = SingleLinkedList()
obj2=SingleLinkedList()
while True:
    n = int(input("\n1.Create\n2.Insert at beginning\n3.insert at mid\n4.insert at end\n5.Display\n6.Delete\n7.Convert\n8.Exit\nEnter a option:"))
    if n == 1:
        c=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if c==1:
            a = int(input("Enter the head value: "))
            n1 = Node(a)
            obj.head = n1
        if c==2:
            a = int(input("Enter the head value: "))
            n1 = Node(a)
            obj2.head = n1
    elif n == 2:
        c=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if c==1:
            b = int(input("Enter a element: "))
            obj.insert_at_beg(b)
        else:
            b = int(input("Enter a element: "))
            obj2.insert_at_beg(b)
    elif n==3:
        a=int(input("Enter the element after which you want to enter:"))
        c=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if c==1:
            b = int(input("Enter a element: "))
            obj.insert_at_mid(a,b)
        else:
            b = int(input("Enter a element: "))
            obj2.insert_at_mid(a,b)
    elif n==4:
        c=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if c==1:
            b = int(input("Enter a element: "))
            obj.insert_at_end(b)
        else:
            b = int(input("Enter a element: "))
            obj2.insert_at_end(b)
    elif n == 5:
        c=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if c==1:
            obj.display()
        else:
            obj2.display()
    elif n == 6:
        d=int(input("1.List 1\n2.List 2\nenter your choice:"))
        if d==1:
            c = int(input("Enter the element you want to delete from the linked list: "))
            obj.delete(c)
        else:
            c = int(input("Enter the element you want to delete from the linked list: "))
            obj.delete(c)
    elif n==7:
        obj.compare()
        obj2.compare()
        l1=[]
        l2=[]
        if l1==l2:
            print("lists are equal")
        else:
            print("list are not equal")
    else:
        break
