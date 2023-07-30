#!/usr/bin/env python3
from brain_games.games import progressions, game_tools


def main():
    game_tools.check_answer(progressions.question_answer, progressions.TASK)
    return


if __name__ == '__main__':
    main()
