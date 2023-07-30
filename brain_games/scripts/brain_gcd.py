#!/usr/bin/env python3
from brain_games.games import gcd, game_tools


def main():
    game_tools.check_answer(gcd.question_answer, gcd.TASK)
    return


if __name__ == '__main__':
    main()
