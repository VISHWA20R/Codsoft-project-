import random
import string

length = int(input("Enter the length of the password: "))

if length >= 6:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)
else:
    print("Enter at least 6 as the password length.")
