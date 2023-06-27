import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(correct_answer, questions):
    for question, ans in zip(questions, correct_answer):
        print(f"Question: {question}")
        user = prompt.string('Your answer:')
        if user != ans:
            print(f"'{user}' is wrong answer ;(. Correct answer was '{ans}'.")
            return False
        print('Correct!')
    return True
