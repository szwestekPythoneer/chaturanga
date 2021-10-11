from tkinter import *
root = Tk ()


def click ():
    a.configure(bg='red')
    text.set('second')


text = StringVar ()
text.set('first')
a = Button (root, textvariable=text, command=click, bg='blue')
a.grid (row=0, column=0)
root.mainloop()