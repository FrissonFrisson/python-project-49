from random import randrange


def question_answer():
    questions = [randrange(1, 100) for i in range(0, 3)]
    correct_answer = ['yes' if i % 2 == 0 else 'no' for i in questions]
    return correct_answer, questions