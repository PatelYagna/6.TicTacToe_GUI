#An interface manager for python. It represents a interface. 
from tkinter import *

#A varibale to use to check if a player X/O has taken turn.
click = True

#This function changes the players turn, and also sends a request to check if a player has won.
def x(buttons):
    global one, two, three, four, five, six, seven, eight, nine, click
    if buttons['text'] == '_' and click==True:
        buttons['text'] = 'X'
        click = False
        win()
    elif buttons["text"] == "_" and click == False:
        buttons["text"] = "O"
        click = True
        win()

#This function has all the win conditions, and if the game is won then it shows a message.
def win():
    global one, two, three, four, five, six, seven, eight, nine
    if (one['text'] == 'X' and two['text'] == 'X' and three['text'] == 'X' or
        four['text'] == 'X' and five['text'] == 'X' and six['text'] == 'X' or
        seven['text'] =='X' and eight['text'] == 'X' and nine['text'] == 'X' or
        one['text'] == 'X' and five['text'] == 'X' and nine['text'] == 'X' or
        three['text'] == 'X' and five['text'] == 'X' and seven['text'] == 'X' or
        one['text'] == 'X' and four['text'] == 'X' and seven['text'] == 'X' or
        two['text'] == 'X' and five['text'] == 'X' and eight['text'] == 'X' or
        seven['text'] == 'X' and six['text'] == 'X' and nine['text'] == 'X'):
        wins=Label(screen, text='You Win X')
        wins.grid()

    elif (one['text'] == 'O' and two['text'] == 'O' and three['text'] == 'O' or
        four['text'] == 'O' and five['text'] == 'O' and six['text'] == 'O' or
        seven['text'] == 'O' and eight['text'] == 'O' and nine['text'] == 'O' or
        one['text'] == 'O' and five['text'] == 'O' and nine['text'] == 'O' or
        three['text'] == 'O' and five['text'] == 'O' and seven['text'] == 'O' or
        one['text'] == 'O' and four['text'] == 'O' and seven['text'] == 'O' or
        two['text'] == 'O' and five['text'] == 'O' and eight['text'] == 'O' or
        seven['text'] == 'O' and six['text'] == 'O' and nine['text'] == 'O'):
        wins=Label(screen, text='You Win O')
        wins.grid()

#This is the main function which keeps the interface running. It also sets up the interface with buttons. 
def main():
    global screen, click
    screen = Tk()
    screen.geometry('285x320')
    screen.title('GameBoard')
    global one, two, three, four, five, six, seven, eight, nine, click
    one = Button(text='_', height = 6, width = 10, command =lambda: x(one))
    one.grid(column=0, row = 0)
    two = Button(text='_', height = 6, width = 10, command=lambda: x(two))
    two.grid(column=1,row=0)
    three = Button(text='_', height = 6, width = 10, command=lambda: x(three))
    three.grid(column=2, row=0)
    four = Button(text='_', height = 6, width = 10, command=lambda: x(four))
    four.grid(column=0, row=1)
    five = Button(text='_', height = 6, width = 10, command=lambda: x(five))
    five.grid(column=1, row=1)
    six = Button(text='_', height = 6, width = 10, command=lambda: x(six))
    six.grid(column=1, row=2)
    seven = Button(text='_', height = 6, width = 10, command=lambda: x(seven))
    seven.grid(column=0, row=2)
    eight = Button(text='_', height = 6, width = 10, command=lambda: x(eight))
    eight.grid(column=2, row=1)
    nine = Button(text='_', height = 6, width = 10, command=lambda: x(nine))
    nine.grid(column=2, row=2)
    screen.mainloop() 
 
#This starts the code.    
main()
