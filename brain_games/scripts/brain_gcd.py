#!/usr/bin/env python3
from . import game_tools
from random import random


def NOD(num_1, num_2):
    n1 = num_1
    n2 = num_2
    while n1 or n2 != 0:
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        a = n1 % n2
        if a == 0:
            return n2
        else:
            n1 = n2
            n2 = a


def main():
    question = [[int(random() * 100), int(random() * 100)] for i in range(0, 3)]
    correct_answer = list([str(NOD(x, y)) for x, y in question])
    question = [f'{x} {y}' for x, y in question]
    name = game_tools.greetings()
    print('Find the greatest common divisor of given numbers.')
    if game_tools.check_answer(correct_answer, question):
        print(f'Congratulations, {name}!')
        return
    print(f"Let's try again, {name}!")
    return


if __name__ == '__main__':
    main()
