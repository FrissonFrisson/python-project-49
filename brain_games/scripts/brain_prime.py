#!/usr/bin/env python3
from brain_games.games import prime
from brain_games import game_tools


def main():
    game_tools.check_answer(prime)
    return


if __name__ == '__main__':
    main()
