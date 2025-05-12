JOKE = "Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
SORRY = "Sorry i will only tell jokes!"

def main():
    user_input = input("Enter Your Word: ")
    if user_input.lower() == "joke" or user_input.lower() == "jokes":
        print(JOKE)
    else:
        print(SORRY)


if __name__ == "__main__":
    main()