#!/usr/bin/env python3
from ..scripts import game_tools
from random import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    questions = list([round(random()*100) for i in range(0, 3)])
    correct_answer = list(['yes'if is_prime(i) else 'no' for i in questions])
    name = game_tools.greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if game_tools.check_answer(correct_answer, questions):
        print(f'Congratulations, {name}!')
        return
    print(f"Let's try again, {name}!")
    return


if __name__ == '__main__':
    main()
