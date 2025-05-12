import random

def main():
    # Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice 1 is: {dice1}, Dice 2 is: {dice2}")
    print(f"Sum of two dice is: {dice1 + dice2}")

if __name__ == "__main__":
    main()