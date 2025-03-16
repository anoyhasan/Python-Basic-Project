import random
import string


def generat_pass(length=8):
    char = string.ascii_letters + string.digits + string.punctuation
    pas = "".join(random.choice(char) for _ in range(length))
    return pas


length = int(input("Enter password length: "))
print(f"Generated Password: {generat_pass(length)}")
