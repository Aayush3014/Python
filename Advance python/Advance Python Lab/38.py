'''38. Write a program to create an arithmetic calculator using tkinter'''

import tkinter as tk
from functools import partial
root=tk.Tk()
root.title("Calculator")
root.geometry("600x600")
def findsum(l3,num1,num2):
    n1=int(num1.get())
    n2=int(num2.get())
    n3=n1+n2
    l3.config(fg="white",bg="black",height=3,width=20,text="Sum=%d"%n3)

def findsub(l3,num1,num2):
    n1=int(num1.get())
    n2=int(num2.get())
    n3=n1-n2
    l3.config(fg="white",bg="black",height=3,width=20,text="Difference=%d"%n3)

def findmul(l3,num1,num2):
    n1=int(num1.get())
    n2=int(num2.get())
    n3=n1*n2
    l3.config(fg="red",bg="yellow",height=3,width=20,text="Product=%d"%n3)

def findmod(l3,num1,num2):
    n1=int(num1.get())
    n2=int(num2.get())
    n3=n1%n2
    l3.config(fg="yellow",bg="blue",height=3,width=20,text="Modulus=%d"%n3)

def finddiv(l3,num1,num2):
    n1=int(num1.get())
    n2=int(num2.get())
    n3=n1/n2
    l3.config(fg="yellow",bg="blue",height=3,width=20,text="Division=%d"%n3)


#Labels
l1=tk.Label(root,text="Enter First Number",fg='red').place(x=20,y=60)
l2=tk.Label(root,text="Enter Second Number",fg='red').place(x=20,y=120)

#TextField
number1=tk.StringVar()  
number2=tk.StringVar()   #use to hold value of textfiled,initially 0
t1=tk.Entry(root,textvariable=number1,bg='yellow',fg='black').place(x=200,y=60)
t2=tk.Entry(root,textvariable=number2,bg='yellow',fg='black').place(x=200,y=120)

labelre=tk.Label(root)
labelre.place(x=200,y=150)
findsum=partial(findsum,labelre,number1,number2)    #partialFunction
findsub=partial(findsub,labelre,number1,number2)    #partialFunction
findmul=partial(findmul,labelre,number1,number2)    #partialFunction
findmod=partial(findmod,labelre,number1,number2)    #partialFunction
finddiv=partial(finddiv,labelre,number1,number2)    #partialFunction
#button

button=tk.Button(root,text="ADD",command=findsum,bg='orange').place(x=50,y=300)
button=tk.Button(root,text="SUB",command=findsub,bg='yellow').place(x=150,y=300)
button=tk.Button(root,text="MUL",command=findmul,bg='green').place(x=250,y=300)
button=tk.Button(root,text="DIV",command=finddiv,bg='cyan').place(x=50,y=350)
button=tk.Button(root,text="MOD",command=findmod,bg='pink').place(x=150,y=350)
button=tk.Button(root,text="EXIT",command=root.destroy,bg='red').place(x=250,y=350)

root.mainloop()