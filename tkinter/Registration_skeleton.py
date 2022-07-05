#Registration Form Skeleton.

from tkinter import *

import tkinter.messagebox as a

root = Tk()
root.title("Registration")
root.geometry('500x500')

def registration():
    
    root2 = Tk()
    root2.title("Entries")
    root2.geometry('500x500')
    
    def submit():
        a.showinfo("Validation Successfull")
        root2.destroy()

    #Labels
    register_f = Label(root2,text = "REGISTRATION FORM",font=40,fg="white",bg="black",width=100).pack()
    st_id = Label(root2,text = "Student ID").place(x=30,y=120)
    st_name = Label(root2,text = "Student Name").place(x=30,y=150)
    ph_num = Label(root2,text = "Phone Number").place(x=30,y=180)
    dep = Label(root2,text = "Department").place(x=30,y=210)
    city = Label(root2,text = "City").place(x=30,y=240)
    E_Add = Label(root2,text = "Email Address").place(x=30,y=270)
    f_name = Label(root2,text = "Father Name").place(x=30,y=300)
    add = Label(root2,text = "Address").place(x=30,y=330)

    #Entries
    st_id_e = Entry(root2).place(x=140,y=120)
    st_name = Entry(root2).place(x=140,y=150)
    ph_num = Entry(root2).place(x=140,y=180)
    dep = Entry(root2).place(x=140,y=210)
    city = Entry(root2).place(x=140,y=240)
    e_add = Entry(root2).place(x=140,y=270)
    f_name = Entry(root2).place(x=140,y=300)
    add = Entry(root2).place(x=140,y=330)

    #Buttons
    butt2 = Button(root2,text = "Submit",fg='white',bg='black',width=10,command=submit).place(x=30,y=360)
    butt3 = Button(root2,text = "Clear",fg='white',bg='black',width=10).place(x=180,y=360)


butt1 = Button(text = "Register",font=30,fg='white',bg='black',command=registration).place(x=200,y=200)

root.mainloop()