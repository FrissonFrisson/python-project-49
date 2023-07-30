WHY = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer(difficulty_settings):
    questions = difficulty_settings()
    correct_answer = 'yes' if questions % 2 == 0 else 'no'
    return correct_answer, questions
