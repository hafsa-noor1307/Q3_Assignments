max_length: int = 3

def shorten(lst):
    removed = []
    while len(lst) > max_length:
        removed.append(lst.pop())
    if removed:
        print("These elements have been removed from the list:", removed)
    
def get_list():
    lst = []
    inp = input("Please enter a value: ")
    while inp != "":
        lst.append(inp)
        inp = input("Please enter a value: ")
    return lst

def main():
    lst = get_list()
    shorten(lst)
    print("The shortened list is:", lst)

if __name__ == "__main__":
    main()
