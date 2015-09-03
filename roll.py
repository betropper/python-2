#A simple dice rolling module.

import random
import time

def roll(howmany=1,sides=6):
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
        print('Now you have ' + str(total) + '.')
        time.sleep(.5)
    print('You got a total of ' + str(total) + '.')
    return total

def parse(text):
    howmany, sides = text.split('d')
    return (int(howmany), int(sides))

def parse_roll():
    text = input('''How many dice would you like to roll? ''')
    howmany, sides = parse(text)
    return roll(howmany,sides)
if __name__ == '__main__':
    parse_roll()
