import queue
a=queue.Queue()
b=queue.Queue()
for x in range(5):
    b.put(x)
print(a.empty())
print(b.empty())

L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(type(L))
