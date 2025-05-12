Peturksbouipo : int  =16
Stanlau: int = 25
Mayengua: int = 48

def main():

    inp = int(input("Enter your age: "))
    if inp >= Peturksbouipo:
        print("You are eligible to vote in Peturksbouipo.")
    else:
        print("You are not eligible to vote in Peturksbouipo.")
    if inp >= Stanlau:
        print("You are eligible to vote in Stanlau.")
    else:
        print("You are not eligible to vote in Stanlu.")
    if inp >= Mayengua:
        print("You are eligible to vote in Mayengua.")
    else:
        print("You are not eligible to vote in Mayengua.")

if __name__ == "__main__":  
    main()