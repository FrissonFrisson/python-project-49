from random import randrange


def question_answer():
    questions = ([randrange(1, 100) for i in range(0, 3)])
    correct_answer = (['yes' if is_prime(i) else 'no' for i in questions])
    return correct_answer, questions


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

    
if __name__ == '__main__':
    main()
