def get_user_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    return numbers

def count_numbers(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts

def print_counts(counts):
    for number, count in counts.items():
        print(f"{number} appears {count} times.")

def main():
    numbers = get_user_numbers()
    counts = count_numbers(numbers)
    print_counts(counts)

if __name__ == "__main__":
    main()