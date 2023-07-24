#!/usr/bin/env python3
from ..games import gcd, game_tools


def main():
    correct_ans, question = gcd.question_answer()
    name = game_tools.greetings()
    print('Find the greatest common divisor of given numbers.')
    game_tools.check_answer(correct_ans, question, name)
    return


if __name__ == '__main__':
    main()
