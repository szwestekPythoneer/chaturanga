from tkinter import *
from board import *
root = Tk ()
root.title ('CZATURANGA')


class BoardButton:
    def __init__(self, text, color, row, column):
        self.text = StringVar ()
        self.text.set (text)
        self.color = color
        self.button = Button (root, textvariable=self.text, command=self.click, bg=color)
        self.button.grid (row=row, column=column)

    def click (self):
        # self.button.configure(bg='red')
        # self.text.set('second')
        pass


buttons = []
for i in range (0, 8):
    for j in range (0, 8):
        buttons.append (BoardButton (board [i][j][-1], board [i][j][:-1], i, j))
die1 = Button (root, text='Rzuć kość.')
die2 = Button (root, text='Rzuć kość')
action = Button (root, text='Poddaj, wieża, roszada.')
redPoints = Label (root, text='Punkty twoje / drużyny.', bg='red')
greenPoints = Label (root, text='Punkty twoje / drużyny.', bg='green')
yellowPoints = Label (root, text='Punkty twoje / drużyny.', bg='yellow')
bluePoints = Label (root, text='Punkty twoje / drużyny.', bg='blue')
die1.grid (row=0, column=8)
die2.grid (row=1, column=8)
action.grid (row=2, column=8)
redPoints.grid (row=3, column=8)
greenPoints.grid (row=4, column=8)
yellowPoints.grid (row=5, column=8)
bluePoints.grid (row=6, column=8)
root.mainloop()
