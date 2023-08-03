from random import randint


TASK = 'What number is missing in the progression?'
MAX_LENGHT_PROGRESSION = 10
MIN_LENGHT_PROGRESSION = 5
MIN_DIFF_PROGRESSION = 1
MAX_NUM = 10
MIN_NUM = 0
START_INDEX = 0


def make_progression(num, lenght, difference):
    if lenght >= MAX_LENGHT_PROGRESSION:
        lenght = MAX_LENGHT_PROGRESSION
    elif lenght <= MIN_LENGHT_PROGRESSION:
        lenght = MIN_LENGHT_PROGRESSION
    if difference < MIN_DIFF_PROGRESSION:
        difference = MIN_DIFF_PROGRESSION
    progression = []
    for i in range(lenght):
        progression.append(str(num))
        num = num + difference
    return progression


def question_answer():
    rndm_num = randint(MIN_NUM, MAX_NUM)
    rndm_lenght = randint(MIN_NUM, MAX_NUM)
    rndm_difference = randint(MIN_NUM, MAX_NUM)
    progression = make_progression(rndm_num, rndm_lenght, rndm_difference)
    index = randint(START_INDEX, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    question = ' '.join(progression)
    return correct_answer, question
