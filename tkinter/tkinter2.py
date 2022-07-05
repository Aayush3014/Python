from tkinter import *

root = Tk()
root.geometry("300x300")
f_name = Label(text="First Name").place(x=20,y=60)
l_name = Label(text="Last Name").place(x=20,y=120)
f_name_e = Entry().place(x=90,y=60)
l_name_e = Entry().place(x=90,y=120)
root.mainloop()