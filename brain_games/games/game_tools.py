import prompt
from random import randrange


# settings_game
NUM_LEVELS = 3
EASY_RANGE = 10
MEDIUM_RANGE = 50
HARD_RANGE = 100
LOWER_RANGE = 0
DIFFICULTY_NAME = 'easy'  # 'easy', 'medium', 'hard'


def difficulty_settings():
    if DIFFICULTY_NAME == 'easy':
        return randrange(LOWER_RANGE, EASY_RANGE)
    elif DIFFICULTY_NAME == 'medium':
        return randrange(LOWER_RANGE, MEDIUM_RANGE)
    elif DIFFICULTY_NAME == 'hard':
        return randrange(LOWER_RANGE, HARD_RANGE)
    else:
        return randrange(LOWER_RANGE, EASY_RANGE)


def check_answer(question_answer, TASK):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(TASK)
    for _ in range(0, NUM_LEVELS):
        correct_answer, questions = question_answer(difficulty_settings)
        print(f'Question: {questions}')
        user_ans = prompt.string('Your answer:')
        if user_ans != str(correct_answer):
            print(
                f'\'{user_ans}\' is wrong answer ;(.',
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
    return
