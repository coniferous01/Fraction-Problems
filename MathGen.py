# The goal of this is to create a program that generats math problems with varying types of challenges.
# Done - I want to come up with mixed practice for adding, subtracting, multiplying, and dividing.
# Done - I want to generate problems with fractions that initially can't be simplified.
# I want to create a way to generate problems where the answers HAVE to be simplified.
# Done - I want to create a way to randomly add in problems that have A SINGLE whole number (so students practice making whole numbers fractions).
# I want to control whether the fractions will include impropper fractions.
# I want to control how many common factors an answer will have (how many times a student needs to simplify their answer).
# I want to be able to make one or multiple values negative

#import libraries
import random

primes = [2, 3, 5, 7, 11, 13, 17, 23]

times = int(input('How many problems do you want?'))

def randf():
    """Generate a random fraction"""
    f1 = random.randint(1,25)
    f2 = random.randint(1,25)
    # I need to come up with a function that tests whether the fraction can be simplified.
    # This entails seeing if BOTH the numberator and denominator can be divided by the SAME factor
    for i in primes:
        while f1%i == 0 and f2%i == 0:
            f1 = random.randint(1,25)
            f2 = random.randint(1,25)

    return(str(f1) + "/" + str(f2))

#print(randf())

def gquestion(f1, f2):
    """Generate an equation with two proper fractions"""
    operation = [' + ', ' - ', ' x ', ' ÷ ']
    return(f1 + operation[random.randint(0,len(operation)-1)] + f2)

def properf():
    """Generate a proper fraction that can't be simplified"""
    denom = random.randint(2,20)
    num = random.randint(1,denom-1)
    n = 1
    while n > 0:
        n -= 1
        for i in primes:
            if denom%i == 0 and num%i == 0:
                n += 1
                num = random.randint(1,denom-1)
        # This approach to programming this relies on a lot of iteration (and possibly too much dependence on the random fxn).
        # How could I structure it so that the initial numbers selected worked (instead of having so much iteration).
    return(str(num) + "/" + str(denom))

#print(properf())

def GenQUnDenom():
    """This fxn generates an equation with two prop. fractions with different denominators"""
    f1 = properf()
    f2 = properf()
    operation = [' + ', ' - ', ' x ', ' ÷ ']
    op = operation[random.randint(0,len(operation)-1)]
    if op == ' ÷ ':
        while f1.split("/")[1] == f2.split("/")[0]:
            f2 = properf()
    else:
        while f1.split("/")[1] == f2.split("/")[1]:
            f2 = properf()
    return((f1 + op + f2 + '\n'))

for i in range(times):
    print(GenQUnDenom())
    
#This is a test
# This is test 2

    


