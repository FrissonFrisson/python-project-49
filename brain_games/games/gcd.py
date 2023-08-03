from math import gcd
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 25
MIN_NUM = 0


def make_question_answer():
    num_1 = randint(MIN_NUM, MAX_NUM)
    num_2 = randint(MIN_NUM, MAX_NUM)
    correct_answer = str(gcd(num_1, num_2))
    question = f'{num_1} {num_2}'
    return correct_answer, question
