roman_map = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
num = int(input("Enter a number to convert to Roman numerals: "))
result = ""
for value, numeral in roman_map:
    while num >= value:
        result += numeral
        num -= value

print("Roman numeral:", result)
