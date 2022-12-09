from tkinter import *
import time
# -------------------- Constants --------------------
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT = 'Courier'
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
CHECK_MARK = '✔'
reps = 0
timer = None
# -------------------- Countdown --------------------
def startCountDown():
    global reps
    time: int
    if reps % 2 == 0:
        time = WORK
        title.config(text='Work', fg=GREEN)
    elif reps % 8 == 7:
        time = LONG_BREAK
        title.config(text='Break', fg=RED)
    else:
        time = SHORT_BREAK
        title.config(text='Break', fg=PINK)
    time *= 60
    countDown(time)
    reps += 1
    marks = ''
    for _ in range(reps // 2):
        marks += CHECK_MARK
    checkMarks.config(text=marks)

def resetTimer():
    global reps
    reps = 0
    window.after_cancel(timer)


def countDown(count=WORK*60):
    global timer
    refreshTimer(count)
    if count > 0:
        timer = window.after(1_000, countDown, count - 1)
    else:
        timer = window.after(1_000, startCountDown)

def refreshTimer(count):
    canvas.itemconfig(timeText, text=toMinute(count))

def toMinute(count):
    minute = count // 60
    second = count % 60
    return f'{"" if minute >= 10 else "0"}{minute}:{"" if second >= 10 else "0"}{second}'
# -------------------- GUI setup --------------------
window = Tk()
window.title('Pomodoro')
window.config(padx=20, pady=20, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT, 54, 'bold'))
title.grid(column=1, row=0)

canvas = Canvas(width=400, height=373, bg=YELLOW, highlightthickness=0)

img = PhotoImage(file='Tomato.png').subsample(2)
canvas.create_image(200, 186, image=img)
timeText = canvas.create_text(200, 240, text='00:00', fill='white', font=(FONT, 36, 'bold'))
canvas.grid(column=1, row=1)

startButton = Button(text='Start', highlightthickness=0, command=startCountDown)
startButton.grid(column=0, row=2)
resetButton = Button(text='Reset', highlightthickness=0, command =resetTimer)
resetButton.grid(column=2, row=2)

checkMarks = Label(text='', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT, 54, 'bold'))
checkMarks.grid(column=1, row=2)

window.mainloop()