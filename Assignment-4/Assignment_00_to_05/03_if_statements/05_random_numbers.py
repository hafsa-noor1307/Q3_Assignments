import random

total_numbers: int = 10
minimum_number: int = 1
maximum_number: int = 100

def main():
    random_number: list[int] = []
    for _ in range(total_numbers):
        random_number.append(random.randint(minimum_number, maximum_number))
    print(f"Random numbers are: {random_number}")

if __name__ == "__main__":
    main()