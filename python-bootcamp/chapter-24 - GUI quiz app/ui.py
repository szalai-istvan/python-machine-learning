from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizBrain: QuizBrain):
        self.gameIsOn = True
        self.quiz = quizBrain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.scoreLabel = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.questionLabel = self.canvas.create_text((150, 150), text='a', font=('Arial', 20, 'italic'), width=280)

        trueImage = PhotoImage(file='images/true.png')
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.checkTrue)
        self.trueButton.grid(row=2, column=0)

        falseImage = PhotoImage(file='images/false.png')
        self.falseButton = Button(image=falseImage, highlightthickness=0,  command=self.checkFalse)
        self.falseButton.grid(row=2, column=1)

        self.getNextQuestion()

        self.window.mainloop()

    def checkTrue(self):
        self.checkAnswer(True)

    def checkFalse(self):
        self.checkAnswer(False)

    def getNextQuestion(self):
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.questionLabel, text=self.question.text)
        else:
            self.canvas.itemconfig(self.questionLabel, text='Out of questions for now. Good game!')
            self.gameIsOn = False

    def checkAnswer(self, answer: bool):
        if not self.gameIsOn:
            return

        if (self.quiz.check_answer(str(answer))):
            self.score += 1
            self.scoreLabel.config(text=f'Score: {self.score}')

        self.getNextQuestion()
