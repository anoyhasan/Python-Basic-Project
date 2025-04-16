def reserveTable():
    userNum = input("How many people are dining ? : ")
    if not userNum.isdigit():
        print("You didn't enter a valid number, restart the process.")
        return
    userNum = int(userNum)
    if userNum == 1:
        guestName1 = input("Enter Guest Name for Confirmation : ")
        print("I Reserve a table for ", guestName1)
    elif userNum == 2:
        guestName1 = input("Enter First Guest Name for Confirmation : ")
        guestName2 = input("Enter Second Guest Name for Confirmation : ")
        print("I Reserve a table for ", guestName1, " and ", guestName2)
    elif userNum == 3:
        guestName1 = input("Enter First Guest Name for Confirmation : ")
        guestName2 = input("Enter Second Guest Name for Confirmation : ")
        guestName3 = input("Enter Third Guest Name for Confirmation : ")
        print(
            "I Reserve a table for ", guestName1, " , ", guestName2, " and ", guestName3
        )
    elif userNum > 3:
        print("Sorry We have maximum capacity 3 Person, restart the process.")
    else:
        print("Wrong Input, restart the process.")


while True:
    choose = input(
        """
        Welcome To Our Restaurant 
                  And 
        Our Maximun capacit is 3 Person per Table

        1.Reserve A Table
        2.Exit
        Make a choose 1 And 2 : """
    )
    if choose == "1":
        reserveTable()
    elif choose == "2":
        print("Thank you for visiting! Goodbye.")
        break
    else:
        break
