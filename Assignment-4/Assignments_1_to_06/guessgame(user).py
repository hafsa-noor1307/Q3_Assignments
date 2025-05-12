import random

def main():
    random_num = random.randint(1,101)
    user_input = int(input("Guess the number: "))
    while random_num != user_input:
        if random_num > user_input:
            print("Low Guess")
        elif random_num < user_input and user_input < 101:
            print("High Guess")
        else:
            print("Enter Numbers below 100")
        user_input = int(input("Guess the number: "))

    print(f"You guess Correct {random_num}")

if __name__ == "__main__":
    main()