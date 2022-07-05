'''40. Write a program to create a window that
disappears automatically after 5 seconds.'''

import tkinter as tk
root = tk.Tk()
root.title("Disappear")
root.geometry("700x500")

tk.Label(root, text="It will Disapper in 5 Second",bg='black',fg='orange').place(x=250,y=150)

root.after(5000, lambda: root.destroy())     # time in ms 5 sec=5000

root.mainloop()
