from random import choice


TASK = 'What is the result of the expression?'


def question_answer(difficulty_settings):
    correct_answers = []
    questions = []
    num_1 = difficulty_settings()
    num_2 = difficulty_settings()
    operator = choice(['*', '+', '-'])
    if operator == '+':
        expression = f'{num_1} {operator} {num_2}'
        value = num_1 + num_2
    elif operator == '-':
        expression = f'{num_1} {operator} {num_2}'
        value = num_1 - num_2
    elif operator == '*':
        expression = f'{num_1} {operator} {num_2}'
        value = num_1 * num_2
    questions = expression
    correct_answers = value
    return correct_answers, questions
