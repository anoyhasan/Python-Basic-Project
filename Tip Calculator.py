def tip_calculator():
    bill_amount = float(input("Enter the bill amount : $"))
    tip_percentage = float(input("Enter the tip percentage : "))
    split_bill = input("Do you want to split the the bill? (yes/no) : ").lower()

    tip = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip
    print(f"The tip is: ${tip:.2f}")
    print(f"The total amount is : $ {total_amount:.2f}")

    if split_bill == "yes":
        num_people = int(input("Enter the number of people to split the bill : "))
        print(f"Each person should pay : ${total_amount/num_people:.2f}")


tip_calculator()
