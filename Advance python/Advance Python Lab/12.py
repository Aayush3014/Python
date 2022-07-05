'''12.Create a class called Complex. Write a menu driven program to read, display,
add and subtract two complex numbers by creating corresponding instance methods.'''

class Complex():

    def read(self):
        self.real1=int(input("Enter real part 1: "))
        self.comp1=int(input("Enter comp part 1: "))
        self.real2=int(input("Enter real part 2: "))
        self.comp2=int(input("Enter comp part 2: "))

    def display(self):
        print("First Complex number C1=",str(self.real1)+"+"+str(self.comp1)+"i")
        print("Second Complex number C2=",str(self.real2)+"+"+str(self.comp2)+"i")
        print()

    def add(self):
        real_sum=self.real1+self.real2
        comp_sum=self.comp1+self.comp2
        print(f"The Sum of Complex Number is : {str(real_sum)} + {str(comp_sum)} i")
        print("\n")
    def subtract(self):
        real_sub=self.real1-self.real2
        comp_sub=self.comp1-self.comp2
        if comp_sub<0:
            print(f"The Subtraction of Complex Number is : {str(real_sub)} + {str(comp_sub)} i")
        else:
            print(f"The Subtraction of Complex Number is : {str(real_sub)} + {str(comp_sub)} i")
        print("\n")
        
C=Complex()
while True:

    print(' 1. Read Complex Number         ')
    print(' 2. Display Complex Number      ')
    print(' 3. Add Two Complex Number      ')
    print(' 4. Subtract Two Complex Number ')
    
    choice=int(input("Enter Your choice from above or Press any key to terminate: "))
    
    if choice==1:
        C.read()
    elif choice==2:
        C.display()
    elif choice==3:
        C.add()
    elif choice==4:
        C.subtract()
    else:
        print("Oops! It is an invalid input.")
        break