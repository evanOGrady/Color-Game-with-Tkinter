import random
from tkinter import *
from tkinter import ttk
score = 0
timeLeft = 30
colorText = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'Brown', 'Purple', 'Gray', 'Orange']


def StartGame(event):
    if (timeLeft == 30):
        Countdown()
    ColorType()

def ColorType():
    global score
    global timeLeft
    if (timeLeft > 0):
        userAnswer.focus_set()
        if (userAnswer.get().lower() == colorText[1].lower()):
            score += 1
        userAnswer.delete(0, END)
        random.shuffle(colorText)
        gameLabel.config(fg= str(colorText[1]), text= str(colorText[0]))

        scoreLabel.config(text="Score: " + str(score))

def Countdown():
    global timeLeft
    if (timeLeft > 0):
        timeLeft -= 1
        timeLabel.config(text="Time Left: " +str(timeLeft))
        timeLabel.after(1000, Countdown)


root = Tk()

root.title("Color Game by Evan O'Grady")
root.geometry("1000x500")
mainLabel = Label(root, text="Type the color of the text below", bg="blue", fg="white", bd=1)
mainLabel.config(font=("Courier", 35))
mainLabel.pack()

scoreLabel = Label(root, text="Press enter to start", font=('Helvetica', 15))
scoreLabel.pack()

timeLabel = Label(root, text="Time Left: " + str(timeLeft), font=('Helvetica', 12))
timeLabel.pack()

gameLabel = Label(root, font= ('Times', 60))
gameLabel.pack()

userAnswer = Entry(root, bd=5)
userAnswer.config(font=(50))

root.bind("<Return>", StartGame)

userAnswer.pack()
userAnswer.focus_set()

root.mainloop()
