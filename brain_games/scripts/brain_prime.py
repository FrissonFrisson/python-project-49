#!/usr/bin/env python3
from brain_games.games import prime, game_tools


def main():
    game_tools.check_answer(prime.question_answer, prime.TASK)
    return


if __name__ == '__main__':
    main()
