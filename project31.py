# Generate random password
import string
import random

length = int(input("enter the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters,k=length))
print(f"Generated password:{password}")