from data import question_data
from question_model import Question
from quiz_brain import Quiz
questions =  []
for q in question_data:
    questions.append(Question(q['text'], q['answer']))

quiz = Quiz(questions)

while quiz.stillHasQuestions():
    print(quiz.getNextQuestion())
    answer = ''
    while not answer in ['True', 'true', 'False', 'false', 't', 'f', 'T', 'F']:
        answer = input('Your answer: ')
    print(quiz.checkAnswer(answer))