import random


def raise_exception ():
    chance = 0.7
    if random.random()< chance:
        raise ValueError('Invalid value')
for _ in range (100):

    try:
        raise_exception()
        print('No exception')
    except ValueError:
        print("value error handled ")



