#fig04_02.py
"""Simulating the dice game scrap"""
import random

def roll_dice():
    """Roll two dice and return theri values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return(die1, die2) #pack die face values into tuple

def display_dice(dice):
    """Display one roll of the two dice"""
    die1, die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')