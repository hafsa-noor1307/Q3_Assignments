import random

def main():
    print("Choose Rock, Paper, or Scissor!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    user = int(input("Enter Your Choice (1/2/3): "))
    comp = random.choice([1, 2, 3])

    Rock, Paper, Scissor = 1, 2, 3 

    if user == Rock and comp == Scissor:
        print("You Win!")
    elif user == Scissor and comp == Paper:
        print("You Win!")
    elif user == Paper and comp == Rock:
        print("You Win!")
    elif user == comp:
        print("It's a Draw!")
    else:
        print("Computer Wins!")

if __name__ == "__main__":
    main()
