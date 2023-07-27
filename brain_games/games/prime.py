from random import randrange

WHY = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def question_answer(difficulty_settings):
    questions = difficulty_settings()
    correct_answer = 'yes' if is_prime(questions) else 'no'
    return correct_answer, questions


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
