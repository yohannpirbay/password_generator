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

print("-" * 55)
print("Welcome to your personal and secure password generator!")
print("-" * 55)

def get_length():
    while True:
        try:
            length = int(input("How long would you like your password to be: "))
            if length < 0:
                print("Please enter a positive number!")
                print()
            elif length < 8:
                print("For a secure password, you must have at least 8 characters!")
                print()
            else:
                return length
        except ValueError:
            print("Please input a number!")
            print()
        except:
            print("Something went wrong, please try again!")

print("Here is your password: " + generate_password(get_length()))
