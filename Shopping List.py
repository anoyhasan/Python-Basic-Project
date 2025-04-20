shopping_list = {}

while True:
    print("\n Shopping List Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Updated Item")
    print("5. Exit")

    choice = input("Choose an Option (1-5) : ")

    if choice == "1":
        item = input("Enter the item name: ")
        qty = input("Enter quantity: ")
        shopping_list[item] = qty
        print(f"{item} added with quantity {qty}.")
    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in shopping_list:
            del shopping_list[item]
            print(f"{item} Removed")
        else:
            print("Item not found.")
    elif choice == "3":
        if shopping_list:
            print("\n Your Shopping List:")
            for item, qty in shopping_list.items():
                print(f"{item} : {qty}")
        else:
            print("Your shopping list is empty.")
    elif choice == "4":
        item = input("Enter item name to update: ")
        if item in shopping_list:
            new_qty = input("Enter new quantity: ")
            shopping_list[item] = new_qty
            print(f"{item} updated to quantity {new_qty}.")
        else:
            print("Item not found")
    elif choice == "5":
        print("Goodbye! Happy shopping!")
        break
    else:
        print("Invalid option. Please choose between 1-5.")
