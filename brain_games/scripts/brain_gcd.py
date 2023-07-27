#!/usr/bin/env python3
from ..games import gcd, game_tools


def main():
    game_tools.check_answer(gcd.question_answer, gcd.WHY)
    return


if __name__ == '__main__':
    main()
