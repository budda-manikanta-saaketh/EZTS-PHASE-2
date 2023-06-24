from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
while True:
    n=int(input("1.push\n2.pop\n3.display\n4.exit\nenter you choice:"))
    if n==1:
        num=int(input("enter the value:"))
        s.put(num)
    if n==2:
        s.get()
    if n==3:
       s.full()
    if n==4:
        break
