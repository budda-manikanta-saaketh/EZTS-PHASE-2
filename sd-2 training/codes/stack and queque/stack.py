stack=[]
def push():
    n=int(input("\nenter an element:"))
    stack.append(n)
    display()
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        x=stack.pop()
        print("removed element:",x)
        display()
def display():
    print(stack)
def top():
    if len(stack)==0:
        print("stack is empty")
    else:
        x=stack[-1]
        print("the top element is",x)
while True:
    n=int(input("1.push\n2.pop\n3.display\n4.exit\n5.top\nenter you choice:"))
    if n==1:
        push()
    if n==2:
        pop()
    if n==3:
        display()
    if n==4:
        top()
    if n==5:
        break