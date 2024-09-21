import random

class Question:
    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct

class Game:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.question)
            for i, answer in enumerate(question.answers, 1):
                print('{}) {}'.format(i, answer))
            answer = int(input('Ваш ответ: '))
            if answer == question.correct:
                print('Верно!')
                self.score += 1                
            else:
                print('Неверно! Правильный ответ: {}'.format(question.answers[question.correct - 1]))
        print('Вы заработали: {}'.format(self.score * 1000))

questions = [
    Question('Какова столица России?', ['Москва', 'Санкт-Петербург', 'Владивосток', 'Минск'], 1),
    Question('Какова столица США?', ['Вашингтон', 'Нью-Йорк', 'Лос-Анджелес', 'Владивосток'], 1),
    Question('Какова столица Франции?', ['Париж', 'Москва', 'Лондон', 'Вена'], 1),
]

game = Game(questions)
game.play()
