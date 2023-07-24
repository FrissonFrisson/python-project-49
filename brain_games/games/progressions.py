from random import randrange


def make_progression():
    random_lenght = randrange(1, 10)
    a = randrange(1, 10)
    d = randrange(1, 10)
    progression = []
    lenght = random_lenght if random_lenght >= 5 else 5
    for i in range(0, lenght):
        progression.append(a)
        a = a + d
    return progression


def question_answer():
    progressions = [make_progression() for i in range(0, 3)]
    questions = []
    correct_answer = []
    for progr in progressions:
        index = randrange(len(progr))
        correct_answer.append(str(progr[index]))
        progr[index] = '..'
        questions.append(progr)
    questions = [' '.join([str(y) for y in i]) for i in questions]
    return correct_answer, questions


if __name__ == '__main__':
    main()
