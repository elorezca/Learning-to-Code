import re

def validate():
    attempts = 3
    while attempts > 0:
        password = input("Please enter a password: ")
        if len(password) < 7:
                print("Make sure you password is at least 7 characters")
                attempts -= 1
        elif re.search('[0-9]', password) is None:
                print("Please include atleast 1 number")
                attempts -= 1
        elif re.search('[^a-zA-Z0-9]', password) is None:
                print("Your password must have at least 1 special character ($, #, @, !, *)")
                attempts -= 1
        elif re.search('[A-Z]', password) is None:
               print("Please include a capitalized letter.")
               attempts -= 1
        else:
                print("Your password meets the criteria.")
                break
        if attempts == 0:
               print("Please try again")

while True:
    print("Welcome to the Password Checker!")
    print("A strong password must meet the following cirteria:")
    print("- At least 7 characters long")
    print("- Include at least 1 special character")
    print("- Include at least 1 number")
    print("- Include at least 1 capitalized letter")
               
        
    validate()

    another = input("Do you want to validate another password? (yes/no): ")
    if another.lower() != "yes":
        break

    # completed