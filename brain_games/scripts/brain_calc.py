#!/usr/bin/env python3
from . import game_tools
from random import random, choice


def main():
    correct_answers = []
    questions = []
    for i in range(0, 3):
        num_1 = int(random() * 10)
        num_2 = int(random() * 10)
        operator = choice(['*', '+', '-'])
        expression = f"{num_1} {operator} {num_2}"
        value = eval(expression)
        questions.append(str(expression)), correct_answers.append(str(value))
    name = game_tools.greetings()
    print('What is the result of the expression?')
    if game_tools.check_answer(correct_answers, questions):
        print(f'Congratulations, {name}!')
        return
    print(f"Let's try again, {name}!")
    return


if __name__ == '__main__':
    main()
