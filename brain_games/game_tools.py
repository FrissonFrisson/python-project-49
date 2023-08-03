import prompt


# settings_game
NUM_LEVELS = 3


def check_answer(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for _ in range(NUM_LEVELS):
        correct_answer, questions = game.question_answer()
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
