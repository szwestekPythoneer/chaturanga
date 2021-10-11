from tkinter import *
from board import *
from random import *
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


def choosePiece1 ():
    figures = ('Król lub pion', 'Słoń', 'Konik', 'Łódź')
    die1text.set(choice (figures))


def choosePiece2 ():
    figures = ('Król lub pion', 'Słoń', 'Konik', 'Łódź')
    die2text.set (choice (figures))


buttons = []
for i in range (0, 8):
    for j in range (0, 8):
        buttons.append (BoardButton (board [i][j][-1], board [i][j][:-1], i, j))
die1text = StringVar ()
die2text = StringVar ()
die1text.set ('Rzuć kość')
die2text.set ('Rzuć kość')
die1 = Button (root, textvariable=die1text, command=choosePiece1)
die2 = Button (root, textvariable=die2text, command=choosePiece2)
action = Button (root, text='Poddaj, wieża, roszada.')
redPoints = Label (root, text='Punkty twoje / drużyny.', bg='red')
greenPoints = Label (root, text='Punkty zielonego / drużyny.', bg='green')
yellowPoints = Label (root, text='Punkty żółtego.', bg='yellow')
bluePoints = Label (root, text='Punkty niebieskiego.', bg='blue')
die1.grid (row=0, column=8)
die2.grid (row=1, column=8)
action.grid (row=2, column=8)
redPoints.grid (row=3, column=8)
greenPoints.grid (row=4, column=8)
yellowPoints.grid (row=5, column=8)
bluePoints.grid (row=6, column=8)
