#!/usr/bin/env python3
from . import game_tools
from random import random


def main():
    questions = list([int(random() * 100) for i in range(0, 3)])
    correct_answer = list(['yes' if i % 2 == 0 else 'no' for i in questions])
    name = game_tools.greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if game_tools.check_answer(correct_answer, questions):
        print(f'Congratulations, {name}!')
        return
    print(f"Let's try again, {name}!")
    return


if __name__ == '__main__':
    main()
