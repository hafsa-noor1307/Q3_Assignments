sentence_start = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    print(f"{sentence_start}{adjective} {noun} {verb}.")

if __name__ == "__main__":
    main()
