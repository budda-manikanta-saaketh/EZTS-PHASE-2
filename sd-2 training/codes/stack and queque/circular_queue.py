class CircularQueue:
    def __init__(self, size):
        #initializing the clas
        self.size = size
        #can use self.queue=[None]*size
        self.queue=[None for i in range[(size)]]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if ((self.rear+1)%self.size==self.front):#size 6 index from 0 to 5
            print("queue is full\n")
        #condition fro empty queue
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at tail place
        else:
            #next position of rear 
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            #condition for empty queue
            print("queue is empty")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        elif (self.rear>=self.front):
            print("elements in the cirular queue end are",end=" ") 
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("elements:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if((self.rear+1)%self.size==self.front):
            print("queue is full")
ob=CircularQueue()
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("delete value=",ob.dequeue())
print("delete value=",ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
#it want be inserted bcs queue full
ob.enqueue(100)        