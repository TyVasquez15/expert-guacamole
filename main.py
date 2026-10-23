
# Name: Tyler Vasquez
# Date: 10/22/2026
# Runs the Tuffy Titan Contact List menu.

import contacts


def print_contact_list(contact_list):
    """Print all contacts in alphabetical order."""
    print("==================== CONTACT LIST ====================")
    print(f'{"Last Name":22}{"First Name":22}{"Phone":12}')
    print(f'{"====================":22}{"====================":22}{"==========":12}')

    for phone, names in contact_list.data.items():
        first_name, last_name = names
        print(f"{last_name:22}{first_name:22}{phone:12}")


def main():
    """Run the Tuffy Titan Contact List application."""
    contact_list = contacts.Contacts(filename="contacts.json")

    while True:
        print("*** TUFFY TITAN CONTACT MAIN MENU")
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list")
        print("5. Set contact filename")
        print("6. Exit the program")

        choice = input("Enter menu choice: ").strip()

        if choice == "1":
            phone = input("Enter phone number: ").strip()
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()

            result = contact_list.add_contact(
                id=phone,
                first_name=first_name,
                last_name=last_name
            )

            if result == "error2":
                print("Phone number already exists.")
            else:
                print(f"Added: {first_name} {last_name}.")

        elif choice == "2":
            phone = input("Enter phone number: ").strip()
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()

            result = contact_list.modify_contact(
                id=phone,
                first_name=first_name,
                last_name=last_name
            )

            if result == "error":
                print("Invalid phone number.")
            else:
                print(f"Modified: {first_name} {last_name}.")

        elif choice == "3":
            phone = input("Enter phone number: ").strip()

            result = contact_list.delete_contact(id=phone)

            if result == "error":
                print("Invalid phone number.")
            else:
                first_name, last_name = result[phone]
                print(f"Deleted: {first_name} {last_name}.")

        elif choice == "4":
            print_contact_list(contact_list)

        elif choice == "5":
            filename = input("Enter contact filename: ").strip()

            if filename:
                contact_list.set_filename(filename=filename)
                print(f"Contact filename set to {filename}.")
            else:
                print("Filename cannot be empty.")

        elif choice == "6":
            break

        else:
            print("Invalid menu choice.")

        print()


if __name__ == "__main__":
    main()
