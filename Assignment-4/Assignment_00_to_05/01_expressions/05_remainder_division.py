def main():
    inp1 = int(input("Enter a number: "))
    inp2 = int(input("Enter another number: "))
    div_result = inp1 // inp2
    result = inp1 % inp2
    print(f"The result of this division is {div_result} with a remainder of {result}.")

if __name__ == "__main__":
    main()