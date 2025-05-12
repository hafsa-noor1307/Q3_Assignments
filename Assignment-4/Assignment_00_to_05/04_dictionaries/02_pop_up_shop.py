fruits = {
    'apple': 10,
    'banana': 15,
    'cherry': 23,
    'date': 12,
    'grape': 18
}

def main():
    print("Welcome to the pop-up shop!")
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount = int(input(f"How many {fruit_name}s would you like to buy? "))
        total_cost += price * amount

    print(f"\nTotal cost of the fruits you bought is {total_cost}$.")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
