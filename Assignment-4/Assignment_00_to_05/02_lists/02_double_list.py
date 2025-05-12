def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    print(f"The numbers are {numbers}")

    for i in range(len(numbers)):
        num_at_index = numbers[i]
        numbers[i] = num_at_index * 2

    print(f"While the double of them are {numbers}")

if __name__ == "__main__":
    main()