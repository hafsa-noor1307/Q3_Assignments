def main():
    user_input = int(input("Enter Number To Double It: "))
    while user_input < 100:
        user_input *= 2
        print(user_input)

if __name__ == "__main__":
    main()