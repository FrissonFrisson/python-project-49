from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def question_answer(difficulty_settings):
    num_1 = difficulty_settings()
    num_2 = difficulty_settings()
    correct_answer = str(gcd(num_1, num_2))
    questions = f'{num_1} {num_2}'
    return correct_answer, questions
