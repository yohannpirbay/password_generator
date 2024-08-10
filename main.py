import random

characters = ['q', 'w', 'e', 'r', 't', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f',
              'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q',
              'W', 'E', 'R', 'T', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G',
              'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '0',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '`', '!',
              '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-',
              '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';',
              '\"', '\'', '<', '>', '.', '?', '/', ',']

password = []

for i in range(16):
    ran_char = random.choice(characters)
    password.append(ran_char)

final_password = ''.join(map(str,password))

print(final_password)

