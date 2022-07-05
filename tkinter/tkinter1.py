from tkinter import *
import tkinter.messagebox as a

root = Tk()
def hello():
    a.showinfo("Welcome to Python class.")
butt1 = Button(text = "Hello",fg = "white",bg = "black",font = 20,command=hello).pack()
root.mainloop()