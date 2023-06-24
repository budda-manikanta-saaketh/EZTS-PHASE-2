#create a stack using user input &extract only even numbers.
stack=[]
def push():
    n=int(input("\nenter an element:"))
    stack.append(n)
    display()
def display():
    print(stack)
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        x=stack.pop()
        print("removed element:",x)
        display()
def extract():
    no=int(input("1.even\n2.odd\nenter your choice:"))
    if no==1:
        for i in range(len(stack)):
            if stack[i]%2==0:
                print(stack[i],end=" ")
    if no==2:
        for i in range(len(stack)):
            if stack[i]%2!=0:
                print(stack[i],end=" ")

while True:
    n=int(input("\n1.push\n2.display\n3.extract\n4.pop\n5.exit\nenter you choice:"))
    if n==1:
        push()
    if n==2:
        display()
    if n==3:
        extract()
    if n==4:
        pop()
    if n==5:
        break