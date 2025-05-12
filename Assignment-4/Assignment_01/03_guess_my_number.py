import random

def main():
    print("I'm Thinking of a Number between 0 - 99")
    random_num = random.randint(0,100)
    user_input = int(input("Enter Your Guess: "))
    while user_input != random_num:
        if user_input > random_num:
            print("Your Guess is too high")
        elif user_input < random_num:
            print("Your Guess is too low")
        user_input = int(input("Enter Your Guess: "))

    print(f"Congrats The Correct answer is {random_num}")

if __name__ == "__main__":
    main()    