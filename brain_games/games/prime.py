from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 25
MIN_NUM = 0


def make_question_answer():
    num = randint(MIN_NUM, MAX_NUM)
    question = num
    correct_answer = 'yes' if is_prime(question) else 'no'
    return correct_answer, question


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
