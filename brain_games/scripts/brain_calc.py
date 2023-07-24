#!/usr/bin/env python3
from ..games import calc, game_tools


def main():
    correct_ans, question = calc.question_answer()
    name = game_tools.greetings()
    print('What is the result of the expression?')
    game_tools.check_answer(correct_ans, question, name)
    return


if __name__ == '__main__':
    main()
