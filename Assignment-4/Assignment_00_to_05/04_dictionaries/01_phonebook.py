'''
In this program we show an example of using dictionaries to keep track of information in a phonebook.
'''

def read_phone_number():
    phonebook = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        phone_number = input("Enter phone number: ")
        phonebook[name] = phone_number

    return phonebook

def print_phonebook(phonebook):
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

def lookup_phone_number(phonebook):
    while True:
        name = input("Enter name to look up: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not found in phonebook.")
        else:
            print(f"{name}'s phone number is {phonebook[name]}.")

def main():
    phonebook = read_phone_number()
    print("Phonebook:")
    print_phonebook(phonebook)
    lookup_phone_number(phonebook)

if __name__ == "__main__":
    main()