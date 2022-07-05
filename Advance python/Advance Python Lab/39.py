'''39. Write a program to draw colored shapes (line, rectangle, oval) on canvas.'''
import tkinter as tk
top=tk.Tk()
top.title("Design")
canvas=tk.Canvas(top,bg='white',height=700,width=1400)

#Designing with rectangle
canvas.create_rectangle(300,600,1100,50,outline='black',fill='red',width=7)
#creating Lines
canvas.create_line(1120,300,1400,300,fill='black',width=10)
#creating oval
canvas.create_oval(0,50,290,590,outline='black',fill='cyan',width=7)
#Creating TextBox
canvas.create_text(140,650,text='OVAL',fill='black',font='bold')
canvas.create_text(700,650,text='RECTANGLE',fill='black',font='bold')
canvas.create_text(1260,350,text='LINE',fill='black',font='bold')

canvas.pack()
top.mainloop()
