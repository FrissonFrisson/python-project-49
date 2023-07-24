#!/usr/bin/env python3
from ..games import progressions, game_tools


def main():
    correct_ans, question = progressions.question_answer()
    name = game_tools.greetings()
    print('What number is missing in the progression?')
    game_tools.check_answer(correct_ans, question, name)
    return


if __name__ == '__main__':
    main()
