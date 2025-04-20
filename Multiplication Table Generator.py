num = int(input("Enter a number: "))
print(f"\nMultiplication Table for {num}:\n")

for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result} ")
