# We use secrets instead of random as it is preferred when generating passwords
import secrets

# Class that handles the logic of password generation
class PasswordLogic:

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
