# TODO: The goal of this is to create a program that generats math problems with varying types of challenges.
# TODO: I want to create a way to generate problems where the answers HAVE to be simplified.
# Done - I want to create a way to add in random problems that have A SINGLE whole number (so students practice making whole numbers fractions).
# TODO: I want to control whether the fractions will include impropper fractions.
# TODO: I want to control how many common factors an answer will have (how many times a student needs to simplify their answer).
# TODO: I want to be able to make one or multiple values negative
# TODO: I need to make sure that the fractions generated don't repeat

import random

primes = [2, 3, 5, 7, 11, 13, 17, 23]

times = input('How many problems do you want? \n')
while True:
    try:
        itimes = int(times)
    except ValueError:
        times = input('Please try entering a number again. \n')
        continue
    else:
        break

whole = input('Do you want any problems with whole numbers? Type "yes" or "no" \n')
while True:
    if whole == 'yes' or whole == 'no':
        break
    else:
        whole = input('Please try again. \n Do you want any problems with whole numbers? Type "yes" or "no" \n')
        continue

def proper_fraction():
    """Generate a proper fraction that can't be simplified"""
    # Can this code be simplified?
    if whole == 'yes':
        denom = random.randint(1, 20)
    else:
        denom = random.randint(2, 20)
    if denom == 1:
        numer = random.randint(1, 20)
    else: 
        numer = random.randint(1, denom-1)
    for i in primes:
        while denom%i == 0 and numer%i == 0:
            if denom == 1:
                numer = random.randint(1, 20)
            else: 
                numer = random.randint(1, denom-1)
    return(str(numer) + "/" + str(denom))

def uncommon_denom_question():
    """Generate an equation with two proper fractions that have different denominators"""
    f1 = proper_fraction()
    f2 = proper_fraction()
    operations = [' + ', ' - ', ' x ', ' ÷ ']
    op = operations[random.randint(0,len(operations)-1)]
    if f1.split("/")[1] == '1':
        f1 = f1.split("/")[0]
    if f2.split("/")[1] == '1':
        f2 = f2.split("/")[0]
    while len(f1.split("/")) < 2 and len(f2.split("/")) < 2:
        f2 = proper_fraction()
    if op == ' ÷ ':
        try:
            while f1.split("/")[1] == f2.split("/")[0]:
                f2 = proper_fraction()
                if f2.split("/")[1] == '1':
                    f2 = f2.split("/")[0]
            return((f1 + op + f2 + '\n'))
        except IndexError:
            return((f1 + op + f2 + '\n'))
    else:
        try:
            while f1.split("/")[1] == f2.split("/")[1]:
                f2 = proper_fraction()
            return((f1 + op + f2 + '\n'))
        except IndexError:
            return((f1 + op + f2 + '\n'))

for i in range(itimes):
    print(uncommon_denom_question())
