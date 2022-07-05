from tkinter import *
master = Tk()
master.geometry('800x700')
w = Canvas(master,width=800,height=700)
w.pack()

w.create_rectangle(100,10,700,600,fill="green2")
w.create_rectangle(310,20,500,150,fill="chocolate1")
w.create_rectangle(350,40,380,60,fill="cyan")
w.create_rectangle(420,40,450,60,fill="cyan")
w.create_oval(395,50,405,80,fill="cyan")
w.create_rectangle(370,100,440,110,fill="red")
w.create_rectangle(350,150,470,300,fill="royal blue")

# vertical line 
w.create_line(380,300,380,400,width=4)
w.create_line(440,300,440,400,width=4)

# horizontal line
w.create_line(380,400,280,400,width=4)
w.create_line(440,400,540,400,width=4)
w.mainloop()