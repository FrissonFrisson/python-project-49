import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(correct_answer, questions):
    for question, answer in zip(questions, correct_answer):
        print(f"Question:{question}")
        user_answer = prompt.string('Your answer:')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            return False
        print('Correct!')
    return True
