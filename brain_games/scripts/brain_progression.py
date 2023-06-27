#!/usr/bin/env python3
from . import game_tools
from random import random, randrange


def progression():
    random_lenght = round(random() * 10)
    a = round(random() * 10)
    d = randrange(1, 10)
    progression = []
    lenght = random_lenght if random_lenght >= 5 else 5
    for i in range(0, lenght):
        progression.append(a)
        a = a + d
    return progression


def main():
    progressions = [progression() for i in range(0, 3)]
    correct_answer = []
    questions = []
    for progr in list(progressions):
        index = randrange(len(progr))
        correct_answer.append(str(progr[index]))
        progr[index] = '..'
        questions.append(progr)
    questions = [' '.join([str(y) for y in i]) for i in questions]
    name = game_tools.greetings()
    print('What number is missing in the progression?')
    if game_tools.check_answer(correct_answer, questions):
        print(f'Congratulations, {name}!')
        return
    print(f"Let's try again, {name}!")
    return


if __name__ == '__main__':
    main()
