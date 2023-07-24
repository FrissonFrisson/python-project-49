#!/usr/bin/env python3
from ..games import prime, game_tools


def main():
    correct_ans, question = prime.question_answer()
    name = game_tools.greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_tools.check_answer(correct_ans, question, name)
    return


if __name__ == '__main__':
    main()
