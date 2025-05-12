# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice 1: {dice1}, Dice 2: {dice2}")
    print(f"Sum of two dice is: {dice1 + dice2}")

def main():
    dice1 : int = 10
    print(f"Initial value of dice1: {dice1}")
    roll_dice()
    roll_dice() 
    roll_dice() 
    print(f"Final value of dice1: {dice1}")

if __name__ == "__main__":  
    main()