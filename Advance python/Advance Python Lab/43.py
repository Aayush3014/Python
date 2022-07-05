'''43. Write a program to display a menu on the menu bar.'''
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Menu Bar Implementation')
root.geometry("600x500")

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File        Ctrl+N', command = None)
file.add_command(label ='Open...           Ctrl+O', command = None)
file.add_command(label ='Save              Ctrl+S', command = None)
file.add_command(label ='Save As         Ctrl+Shift+S', command = None)
file.add_separator()
file.add_command(label ='Print          Ctrl+P', command = None)
file.add_command(label ='Recent Files...', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
file.add_separator()
file.add_separator()
file.add_command(label ='Designed By Shivesh', command = None)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Search Menu and commands
search = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Search', menu = search)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# Adding name Menu and commands
user = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='contact Shivesh', menu = user)
user.add_command(label = "contact",command=None)
user.add_command(label = "mail",command=None)
user.add_command(label = "terminate",command=root.destroy)



# display Menu
root.config(menu = menubar)
mainloop()
