#!/usr/bin/env python3
from ..games import progressions, game_tools


def main():
    game_tools.check_answer(progressions.question_answer, progressions.WHY)
    return


if __name__ == '__main__':
    main()
