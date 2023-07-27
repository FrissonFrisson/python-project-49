#!/usr/bin/env python3
from ..games import even, game_tools


def main():
    game_tools.check_answer(even.question_answer, even.WHY)
    return


if __name__ == '__main__':
    main()
