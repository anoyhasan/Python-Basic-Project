# contacts = {
#     "anoy": {"phone": "123-456-7890", "email": "john@example.com"},
#     "hasan": {"phone": "987-654-3210", "email": "jane@example.com"},
# }


def display_menu():
    print("\n Contact Book ")
    print("1. Add a contact.")
    print("2. Remove a contact.")
    print("3. Updated contacts")
    print("4. View all contacts")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter the name : ")
    phone = input("Enter the Phone number : ")
    email = input("Enter the Email : ")

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} Added")


def remove_contact(contacts):
    name = input("Enter the name of the contact to remove : ")

    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed")
    else:
        print("Contact not found!")


def updated_contact(contacts):
    name = input("Enter the name of the contact to edit:")
    if name in contacts:
        print(f"Editing {name}'s contact")
        print(f"Current phone: {contacts[name]['phone']}")
        print(f"Current email: {contacts[name]['email']}")
        phone = input(
            "Enter new phone number (or press Enter to keep the current phone): "
        )
        email = input("Enter new email (or press Enter to keep the current email): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print(f"{name}'s contact updated!")
    else:
        print("Contact not found!")


def view_contact(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("---")
    else:
        print("No contacts available.")


def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            remove_contact(contacts)
        elif choice == "3":
            updated_contact(contacts)
        elif choice == "4":
            view_contact(contacts)
        elif choice == "5":
            print("GoodBye")
            break
        else:
            print("Invalid choice. Please try again.")


main()
