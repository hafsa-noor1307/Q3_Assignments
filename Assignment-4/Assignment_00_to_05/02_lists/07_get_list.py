def main():
    my_list = []
    
    inp = input("Please enter a value: ")
    while inp != "":
        my_list.append(inp)
        inp = input("Please enter a value: ")
    print("The list is:", my_list)
    return my_list

if __name__ == "__main__":
    main()