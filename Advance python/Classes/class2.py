class myclass:
    def __init__(self,val = 0):
        self.l = []
        for i in range(val):
            self.l.append(i)
    def __str__(self):
        return 'L:%s'%(str(self.l))
    def method1(self,x= 0):
        for i in range(len(self.l)):
            self.l[i] = x * self.l[i]
        return self.l
    def method2(self,i=0):
        if i in range(len(self.l)):
            return self.l[i]
        else:
            return None
inst1 = myclass()
print(inst1)
inst2=myclass(3)
print(inst2)
print(inst1.method1(2))
print(inst2.method2(1))