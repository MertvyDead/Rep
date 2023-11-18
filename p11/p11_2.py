import random
import string

def generate_password(length, uppercase = False, special_crc = False;):
    if uppercase:
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        return password
print(generate_password(12))


