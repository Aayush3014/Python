##Password checker working. 


from tkinter import *

import tkinter.messagebox as a

win=Tk()

#for username
entrya=Entry(win)
entrya.config(bg='red',fg='blue',width=26,font='30')
entrya.grid(row=1,column=2)

#for password
entry=Entry(win,show='* ')
entry.config(bg='red',fg='blue',width=26,font='30')
entry.grid(row=2,column=2)

def but1():
    
    if entry.get()=='password' and entrya.get()=='ayush':
        a.showinfo("Welcome")
        win.destroy()
    
    else:
        
        a.showinfo('busted!!!!!!','wrong password')
        win.destroy()

button=Button(win,text='confirm',command=but1,width=19,bg='blue',fg='red',font='ariel 16')
button.grid(row=3,column=1)

def but2():
    
    entry.delete(0,'end')
    entrya.delete(0,'end')

lable1=Label(win,bg='black',fg='blue',text='Username',font='bold',width='26').grid(row=1,column=1)
lable2=Label(win,bg='black',fg='blue',text='password',font='bold',width='26').grid(row=2,column=1)

button2=Button(win,text='clear',command=but2,bg='blue',fg='red',font='ariel 16',width=19)
button2.grid(row=3,column=2)

win.mainloop()