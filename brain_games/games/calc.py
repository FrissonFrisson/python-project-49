from random import choice, randint


TASK = 'What is the result of the expression?'
MAX_NUM = 10
MIN_NUM = 0


def make_question_answer():
    correct_answer = ''
    question = ''
    num_1 = randint(MIN_NUM, MAX_NUM)
    num_2 = randint(MIN_NUM, MAX_NUM)
    operator = choice(['*', '+', '-'])
    expression = f'{num_1} {operator} {num_2}'
    if operator == '+':
        value = num_1 + num_2
    elif operator == '-':
        value = num_1 - num_2
    else:
        value = num_1 * num_2
    question = expression
    correct_answer = value
    return correct_answer, question
