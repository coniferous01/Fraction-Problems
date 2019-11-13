# The goal of this is to create a program that generats math problems with varying types of challenges.
# I want to create a way to generate problems where the answers HAVE to be simplified.
# Done - I want to create a way to randomly add in problems that have A SINGLE whole number (so students practice making whole numbers fractions).
# I want to control whether the fractions will include impropper fractions.
# I want to control how many common factors an answer will have (how many times a student needs to simplify their answer).
# I want to be able to make one or multiple values negative
# I need to make sure that the fractions generated don't repeat

import random

primes = [2, 3, 5, 7, 11, 13, 17, 23]

times = int(input('How many problems do you want? \n'))

def properf():
    """Generate a proper fraction that can't be simplified"""
    denom = random.randint(1, 20)
    if denom == 1:
        num = random.randint(1, 20)
    else: 
        num = random.randint(1, denom-1)
    n = 1
    while n > 0:
        n -= 1
        for i in primes:
            if denom%i == 0 and num%i == 0:
                n += 1
                num = random.randint(1, denom-1)
    return(str(num) + "/" + str(denom))

def GenQUnDenom():
    """Generate an equation with two proper fractions that have different denominators"""
    f1 = properf()
    f2 = properf()
    operations = [' + ', ' - ', ' x ', ' ÷ ']
    op = operations[random.randint(0,len(operations)-1)]
    if f1.split("/")[1] == '1':
        f1 = f1.split("/")[0]
    if f2.split("/")[1] == '1':
        f2 = f2.split("/")[0]
    while len(f1.split("/")) < 2 and len(f2.split("/")) < 2:
        f2 = properf()
    if op == ' ÷ ':
        try:
            while f1.split("/")[1] == f2.split("/")[0]:
                f2 = properf()
                if f2.split("/")[1] == '1':
                    f2 = f2.split("/")[0]
            return((f1 + op + f2 + '\n'))
        except IndexError:
            return((f1 + op + f2 + '\n'))
    else:
        try:
            while f1.split("/")[1] == f2.split("/")[1]:
                f2 = properf()
            return((f1 + op + f2 + '\n'))
        except IndexError:
            return((f1 + op + f2 + '\n'))

for i in range(times):
    print(GenQUnDenom())