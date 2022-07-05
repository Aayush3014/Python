'''41. Write a program to create a button and a label inside the frame
widget. Button should change the color upon hovering over the button and label
should disappear on clicking the button.'''

import tkinter as tk
class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.title("Question_41")
       self.root.geometry("700x600")
       self.label=tk.Label(self.root,
                           text = "Label will disappear if you click this button")
       self.buttonForget = tk.Button(self.root,fg='orange',bg='black',
                          text = 'Click me to disable Label',
                          command=lambda:self.label.destroy()) 
       
       self.buttonForget.pack()
       self.buttonForget.place(x=260,y=280)
       
       self.label.pack()
       self.label.place(x=240,y=220)
       self.root.mainloop()
    
app = Test()
