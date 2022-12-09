from tkinter import *
import pandas
import random as rndm

BACKGROUND_COLOR = "#B1DDC6"
DATA = pandas.read_csv('data/french_words.csv').to_dict(orient='records')

timer = None
choice = None

def nextCard():
    global timer, choice
    canvas.itemconfig(canvasBackground, image=cardFrontImage)
    choice = rndm.choice(DATA)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=choice['French'], fill='black')
    if not timer is None:
        window.after_cancel(timer)
    timer = window.after(3_000, flipCard, choice)

def flipCard(choice):
    canvas.itemconfig(canvasBackground, image=cardBackImage)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=choice['English'], fill='white')

def isKnown():
    if len(DATA) > 1:
        DATA.remove(choice)
        nextCard()
    else:
        window.after_cancel(timer)
        canvas.itemconfig(canvasBackground, image=cardBackImage)
        canvas.itemconfig(title, text='Congratulations!', fill='white')
        canvas.itemconfig(word, text='You have finished!', fill='white')

window = Tk()
window.title('Flash cards')
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
cardFrontImage = PhotoImage(file='images/card_front.png')
cardBackImage = PhotoImage(file='images/card_back.png')
canvasBackground = canvas.create_image(400, 263, image=cardFrontImage)

title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file='images/wrong.png')
wrongButton = Button(image=wrong, highlightthickness=0, command=nextCard)
wrongButton.grid(row=1, column=0)

right = PhotoImage(file='images/right.png')
rightButton = Button(image=right, highlightthickness=0, command=isKnown)
rightButton.grid(row=1, column=1)

nextCard()
window.mainloop()