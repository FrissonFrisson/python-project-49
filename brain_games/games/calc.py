from random import randrange, choice


def question_answer():
    correct_answers = []
    questions = []
    for i in range(0, 3):
        num_1 = randrange(1, 100)
        num_2 = randrange(1, 100)
        operator = choice(['*', '+', '-'])
        expression = f'{num_1} {operator} {num_2}'
        value = eval(expression)
        questions.append(str(expression)), correct_answers.append(str(value))
    return correct_answers, questions