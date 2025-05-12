minimun_height: int = 50

def main():
    height: int = int(input("Enter your height in inches: "))
    if height >= minimun_height:
        print("You are tall enough to ride the roller coaster!")
    else:
        print("You are not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()