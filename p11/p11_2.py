import random
import string

import random
import string
def get_random_password(lenght=10,uppercase=False,special_chars=False, nums = False):
    source=[]
    password=''
    source+=list(string.ascii_lowercase)
    if uppercase:
        source+=list(string.ascii_uppercase)
    if special_chars:
        source+=list(string.punctuation)
    if nums:
        source+=list(string.digits)
    for i in range(lenght):
        password+=random.choice(source)
    return password
print(get_random_password(24, uppercase=True,special_chars=True, nums=True))



