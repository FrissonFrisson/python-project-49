import prompt


def greetings():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(correct_answer, questions, name):
    for question, ans in zip(questions, correct_answer):
        print(f'Question: {question}')
        user_ans = prompt.string('Your answer:')
        if user_ans != ans:
            print(
                f'\'{user_ans}\' is wrong answer ;(.',
                f'Correct answer was \'{ans}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
    return
