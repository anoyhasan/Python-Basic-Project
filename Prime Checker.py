def prime_checker(number):

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


num = int(input("Enter a number : "))

if prime_checker(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
