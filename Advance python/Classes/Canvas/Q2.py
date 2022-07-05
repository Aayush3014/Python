from tkinter import *
master = Tk()
w = Canvas(master,width=1400,height=700)
w.pack()
w.create_rectangle(320,620,1120,70,fill="green")
w.create_rectangle(402,550,1038,140,fill="pink")
w.create_rectangle(479,490,960,200,fill="yellow")
w.create_rectangle(570,420,870,270,fill="blue")

w.create_line(320,70,570,270,fill="black",width=4)
w.create_line(1120,70,870,270,fill="black",width=4)
w.create_line(320,620,570,420,fill="black",width=4)
w.create_line(1120,600,870,420,fill="black",width=4)

w.create_oval(20,70,320,620,fill="firebrick2")
w.create_oval(1120,70,1390,620,fill="pale green")

w.create_rectangle(20,400,320,290,fill="violet")
w.create_rectangle(1120,400,1390,290,fill="violet")
w.mainloop()