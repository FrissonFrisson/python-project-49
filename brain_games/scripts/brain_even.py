#!/usr/bin/env python3
from ..games import even, game_tools


def main():
    correct_ans, question = even.question_answer()
    name = game_tools.greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_tools.check_answer(correct_ans, question, name)
 

if __name__ == '__main__':
    main()
