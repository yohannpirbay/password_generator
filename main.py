import secrets

lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/'

chars = lowercase_chars + uppercase_chars + numbers + special_chars

def generate_password(length):

    password = [secrets.choice(lowercase_chars),
                secrets.choice(uppercase_chars),
                secrets.choice(numbers),
                secrets.choice(special_chars)]
    
    for i in range(length - 4):
        password.append(secrets.choice(chars))
    
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def get_length():
    while True:
        try:
            length = int(input("How long would you like your password to be: "))
            print()
            if length < 0:
                print("Please enter a positive number!")
                print()
            elif length < 8:
                print("For a secure password, you must have at least 8 characters!")
                print()
            else:
                return length
        except ValueError:
            print()
            print("Please input a number!")
            print()
        except:
            print("Something went wrong, please try again!")

def welcome():
    print("-" * 55)
    print("Welcome to your personal and secure password generator!")
    print("-" * 55)
    print()

def display_password(length):
    print("Here is your password: " + generate_password(length))
    print()

def regenerate():
    while True:
        answer = input("Would you like to generate a new password (y/n)? ").lower()
        print()
        if answer not in ['y', 'n']:
            print("Please chose between 'y' or 'n'!")
            print()
        else:
            return answer == 'y'
        
def end_message():
    print("Thanks for using our tool :)")

def start():
    welcome()
    while True:
        length = get_length()
        display_password(length)
        if regenerate():
            continue
        else:
            end_message()
            return
        

start()

