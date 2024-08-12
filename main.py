# We use secrets instead of random as it is preferred when generating passwords
import secrets 

# Character sets
lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/'

chars = lowercase_chars + uppercase_chars + numbers + special_chars

# Generates a password of given length
def generate_password(length):

    password = [secrets.choice(lowercase_chars),
                secrets.choice(uppercase_chars),
                secrets.choice(numbers),
                secrets.choice(special_chars)]
    
    for i in range(length - len(password)):
        password.append(secrets.choice(chars))
    
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# Gets user input for the wanted length of the password
def get_length():
    while True:
        try:
            length = int(input("How long would you like your password to be: "))
            print()
            if length < 0:
                print("Please enter a positive number!\n")
            elif length < 8:
                print("For a secure password, you must have at least 8 characters!\n")
            else:
                return length
        except ValueError:
            print("\nPlease input a number!\n")
        except:
            print("\nSomething went wrong, please try again!\n")

# Displays a welcome message
def welcome():
    print("-" * 55)
    print("Welcome to your personal and secure password generator!")
    print("-" * 55 + "\n")

# Displays the generated password
def display_password(length):
    print("Here is your password: " + generate_password(length) + "\n")

# Asks if the user wants to generate a new password
def regenerate():
    while True:
        answer = input("Would you like to generate a new password (y/n)? ").lower()
        print()
        if answer not in ['y', 'n']:
            print("Please chose between 'y' or 'n'!\n")
        else:
            return answer == 'y'

# Displays an end message  
def end_message():
    print("Thanks for using my tool :)")

# Main function to start the program
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

