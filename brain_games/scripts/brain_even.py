#!/usr/bin/env python3
from brain_games.games import even, game_tools


def main():
    game_tools.check_answer(even.question_answer, even.TASK)
    return


if __name__ == '__main__':
    main()
