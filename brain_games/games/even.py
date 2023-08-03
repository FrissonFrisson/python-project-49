from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUM = 50
MIN_NUM = 0


def make_question_answer():
    num = randint(MIN_NUM, MAX_NUM)
    question = num
    correct_answer = 'yes' if is_even(num) else 'no'
    return correct_answer, question


def is_even(num):
    if num % 2 == 0:
        return True
    return False
