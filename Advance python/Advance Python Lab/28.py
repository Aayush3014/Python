'''28. WAP to create a Complex class having real and imaginary as it attributes.
Overload the +,-,/,* and += operators for objects of Complex class'''
class Complex():
    def __init__(self):
        self.real = 0 
        self.imag = 0
    def setValue(self,real,imag):
        self.real = real
        self.imag = imag
    #Overloading the + Operataor
    def __add__(self,C):
        Temp=Complex()
        Temp.real = self.real + C.real
        Temp.imag = self.imag + C.imag
        print("(",Temp.real,'+',Temp.imag,'i)')
    #Overloading the - Operataor
    def __sub__(self,C):
        Temp=Complex()
        Temp.real = self.real - C.real
        Temp.imag = self.imag - C.imag
        print("(",Temp.real,'-',Temp.imag,'i)')
    #Overloading the / Operataor
    def __truediv__(self,C):
        Temp=Complex()
        Temp.real = self.real / C.real
        Temp.imag = self.imag / C.imag
        print("(",round(Temp.real,2),'/',Temp.imag,'i)')
    #Overloading the * Operataor
    def __mul__(self,C):
        Temp=Complex()
        Temp.real = self.real * C.real
        Temp.imag = self.imag * C.imag
        print("(",Temp.real,'*',Temp.imag,'i*i)')
    #Overloading the += Operataor
    def __iadd__(self,C):
        Temp=Complex()
        self.real += C.real
        self.imag += self.imag + C.imag
        print("(",self.real,'+',self.imag,'i)')
    def __repr__(self):
        return self.real,self.imag

        
C1 = Complex()
C1.setValue(1,2)
C2 = Complex()
C2.setValue(3,4)
C3 = Complex()
C3 = C1+C2
C4 = Complex()
C4 = C1-C2
C5 = Complex()
C5 = C1/C2
C6 = Complex()
C6 = C1*C2
C1 += C2
