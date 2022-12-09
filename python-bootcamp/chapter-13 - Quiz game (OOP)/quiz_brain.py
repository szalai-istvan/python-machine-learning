import question_model
import random

class Quiz:
    def __init__(self, questions: list[question_model.Question]):
        self.questionNumber = 0
        self.correctAnswers = 0
        self.questions = questions
        self.currentQuestion = question_model.Question

    def getNextQuestion(self) -> str:
        self.questionNumber += 1
        self.currentQuestion = random.choice(self.questions)
        self.questions.remove(self.currentQuestion)
        return f'[Q{self.questionNumber}] {self.currentQuestion}'

    def checkAnswer(self, answer: str) -> str:
        if self.currentQuestion.answer.lower()[0] == answer.lower()[0]:
            self.correctAnswers += 1
            return 'Correct!'
        return 'Wrong!'

    def stillHasQuestions(self) -> bool:
        if len(self.questions) > 0 and self.questionNumber < 10:
            return True
        print(f'You got {self.correctAnswers}/{self.questionNumber} right. Nice job!')
        return False