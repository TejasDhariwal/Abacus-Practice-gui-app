# this file consists of the functions that define logic behind the generation of the questions of different arena.
from random import randint, choice

def MultipyQuesGen(count, digit):
    questions = []
    answers = []

    for i in range(count):
        v1 = randint(10**(digit-1), (10**digit)-1)
        v2 = randint(10**1, (10**2)-1)

        question = f"{i+1}. {v1} X {v2} = "
        answer = v1*v2

        questions.append(question)
        answers.append(answer)
    
    return questions, answers

def DivisionQuesGen(count, digit):
    questions = []
    answers = []

    for i in range(count):
        v1 = randint(10**(digit-1), (10**digit)-1)
        v2 = randint(10**1, (10**2)-1)

        question = f"{i+1}. {v1} / {v2} = "
        answer = v1//v2

        questions.append(question)
        answers.append(answer)
    
    return questions, answers

def DecimalQuesGen(count, digit):
    questions = []
    answers = []

    for i in range(count):
        question = []
        answer = 0
        for j in range(5):
            num = randint(10**(digit-1), (10**digit)-1)
            val = f"{choice(['  ', '-'])}{num}"
            question.append(f"{val[:-2]}.{val[-2:]}")

            if '-' in val:
                answer -= num
            else:
                answer += num

        questions.append(question)
        answers.append(f"{str(answer)[:-2]}.{str(answer)[-2:]}")
    
    return questions, answers


def CalcQuesGen(count, digit):
    questions = []
    answers = []

    for i in range(count):
        question = []
        answer = 0
        for j in range(5):
            num = randint(10**(digit-1), (10**digit)-1)
            val = f"{choice(['  ', '-'])}{num}"
            question.append(val)

            if '-' in val:
                answer -= num
            else:
                answer += num

        questions.append(question)
        answers.append(answer)
    
    return questions, answers

def BasicsQuesGen(abacus, mental):
    questions = []
    answers = []

    for i in range(8):
        if i >= 4:
            val = f"{choice(['+', '-'])}{randint(10**(mental-1), (10**mental)-1)}"
        else:
            val = f"{choice(['+', '-'])}{randint(10**(abacus-1), (10**abacus)-1)}"
        
        
        questions.append(val)
        
    
    return questions

    