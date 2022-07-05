class Queue:
    
    def __init__(self):
        self.q = []
        self.front = None
    
    def enqueue(self,item):
        self.q.append(item)
        if (len(self.q) ==1):
            self.front = self.rear = 0
        else:
            self.rear = len(self.q) - 1
    
    def isempty(self):
        if (self.q == []):
            return True
        else:
            return False
    def dequeue(self):
        if (a.isempty()):
            return "underflow"
        else:
            self.ite = self.q.pop(0)
        
        if (len(self.q) == 0):
            self.front = self.rear = None
        return self.ite
    def display(self):
        if (a.isempty()):
            print("Queue empty")
        elif (len(self.q) == 1):
            print(self.q[0], "<== front,rear")
        else:
            self.front = 0 
            self.rear = len(self.q)-1
            print(self.q[self.front],"<--front")
            for t in range(1,self.rear):
                print(self.q[t])
            print(self.q[self.rear],"<--rear")

a = Queue()
while True:
    print("""queue operations
    1:enqueue
    2:dequeue
    3:display
    4: Exit""")

    n = int(input("Enter choice : "))
    if n == 1:
        val = int(input("Enter item"))
        a.enqueue(val)
        input("press any key to continue")
    if n == 2:
        returnvalue = a.dequeue()
        if (returnvalue == "underflow"):
            print("queue is empty")
        else:
            print("dequed item =",returnvalue)
        input("press any key to continue")
    if n == 3:
        a.display()
    if n == 5 :
        break