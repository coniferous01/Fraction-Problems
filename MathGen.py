# TODO: The goal of this is to create a program that generates math problems with varying types of challenges.
# TODO: I want to create a way to generate problems where the answers HAVE to be simplified.
# TODO: I want to control whether the fractions will include improper fractions.
# TODO: I want to control how many common factors an answer will have (how many times a student needs to simplify their answer).
# TODO: I want to be able to make one or multiple values negative
# TODO: I need to make sure that the fractions generated don't repeat

import random
from numpy.random import choice

primes = [2, 3, 5, 7, 11, 13, 17, 23]

times = input('How many problems do you want? \n')

negative = input('What percentage of the problems do you want to have negative numbers? Enter a number 0 - 100.\n')
while True:
    try:
        negative_float = float(negative)/100
    except ValueError:
        negative = input('Please try entering a percentage again. \n')
        continue
    else:
        break

while True:
    try:
        i_times = int(times)
    except ValueError:
        times = input('Please try entering a number again. \n')
        continue
    else:
        break

whole = input('Do you want any problems with whole numbers? Type "yes" or "no" \n')
while True:
    if whole.lower() == 'yes' or whole.lower() == 'no':
        break
    else:
        whole = input('Please try again. \n Do you want any problems with whole numbers? Type "yes" or "no" \n')
        continue

def proper_fraction():
    """Generate a proper fraction that can't be simplified"""
    # NTS - Can this code be simplified?
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
    #r = random.random()
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
            return((f1 + op + f2 + ' \n'))
        except IndexError:
            return((f1 + op + f2 + ' \n'))
    else:
        try:
            while f1.split("/")[1] == f2.split("/")[1]:
                f2 = proper_fraction()         
            return((f1 + op + f2 + ' \n'))
        except IndexError:
            return((f1 + op + f2 + ' \n'))

l_problems = []

for i in range(i_times):
    l_problems.append(uncommon_denom_question())

negative_number = int(negative_float*i_times)
negative_problems = l_problems[:negative_number]
positive_problems = l_problems[negative_number:]

for problem in negative_problems:
    if 0.5 >= random.random():
        split_problem = '(-' + problem.split()[0] + ')'
        n_problem = split_problem + ' ' + problem.split()[1] + ' ' + problem.split()[2] + ' \n'
        r_place = random.randint(0, len(l_problems))
        positive_problems.insert(r_place, n_problem)
    else:
        split_problem = '(-' + problem.split()[-1] + ')'
        n_problem = problem.split()[0] + ' ' + problem.split()[1] + ' ' + split_problem + ' \n'
        r_place = random.randint(0, len(l_problems))
        positive_problems.insert(r_place, n_problem)

print(positive_problems)

#Done - Next task is to change code so that either term will be negative (not just the first one)
