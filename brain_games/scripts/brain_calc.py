#!/usr/bin/env python3
from ..games import calc, game_tools


def main():
    game_tools.check_answer(calc.question_answer, calc.WHY)
    return


if __name__ == '__main__':
    main()
