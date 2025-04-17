def bmi_calculator():
    weight = float(input("Enter you weight in kg : "))
    height = float(input("Enter you height in meters : "))

    bmi = weight / (height**2)
    print(f"You BMI is  {bmi:.2f}")

    if bmi < 18.5:
        print("You are Underweight")
    elif bmi <= 24.5:
        print("You are Normal weigh")
    elif bmi <= 29.9:
        print("You are Overweight")
    else:
        print("You are Obesity")


bmi_calculator()
