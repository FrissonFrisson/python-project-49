from random import randrange
from math import gcd

def question_answer():
    questions = [[randrange(1, 100), randrange (1, 100)] for i in range(0, 3)]
    correct_answer = [str(gcd(x, y)) for x, y in questions]
    questions = [f'{x} {y}' for x, y in questions]
    return correct_answer, questions