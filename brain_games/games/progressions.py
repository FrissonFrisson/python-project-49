from random import randrange


TASK = 'What number is missing in the progression?'
MAX_LENGHT_PROGRESSION = 10
MIN_LENGHT_PROGRESSION = 5
MIN_DIFF_PROGRESSION = 1


def make_progression(difficulty_settings):
    rndm_lenght = difficulty_settings()
    if rndm_lenght >= MAX_LENGHT_PROGRESSION:
        rndm_lenght = MAX_LENGHT_PROGRESSION
    elif rndm_lenght <= MIN_LENGHT_PROGRESSION:
        rndm_lenght = MIN_LENGHT_PROGRESSION
    num = difficulty_settings()
    difference = difficulty_settings()
    if difficulty_settings() < MIN_DIFF_PROGRESSION:
        difference = MIN_DIFF_PROGRESSION
    progression = []
    for i in range(rndm_lenght):
        progression.append(str(num))
        num = num + difference
    return progression


def question_answer(difficulty_settings):
    progression = make_progression(difficulty_settings)
    index = randrange(len(progression))
    correct_answer = progression[index]
    progression[index] = '..'
    questions = ' '.join(progression)
    return correct_answer, questions
