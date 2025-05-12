class InvalidAgeError(Exception):
    pass

def check_age(age):
    try:
        if age >= 18:
            print("You're Eligble")
        else:
            raise InvalidAgeError("You're Not Eligible For It Sorry!")
        
    except InvalidAgeError as e:
        print(e)


user_input = int(input("Enter Your Age: "))
check_age(user_input)

