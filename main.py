# Name: Tyler Vasquez
# Date: 9/20/2026
#Main driver program for the employee contact list.

import contacts

def main():
    # Run the employee contact list program.
    contact_list = {}

    while True:
        print("\n*** EMPLOYEE CONTACT MAIN MENU")
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list")
        print("5. Find contact")
        print("6. Exit the program")

        choice = input("Enter menu choice: ").strip()

        if choice == "1":
            phone_number = input("Enter phone number: ").strip()

            try:
                phone_number = int(phone_number)
            except ValueError:
                print("Invalid phone number.")
                continue

            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()

            result = contacts.add_contact(
                contact_list,
                id=phone_number,
                first_name=first_name,
                last_name=last_name
            )

            if isinstance(result, str):
                print(result)
            else:
                print(f"Added: {result[0]} {result[1]}.")

        elif choice == "2":
            phone_number = input("Enter phone number: ").strip()

            try:
                phone_number = int(phone_number)
            except ValueError:
                print("Phone number does not exist.")
                continue

            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()

            result = contacts.modify_contact(
                contact_list,
                id=phone_number,
                first_name=first_name,
                last_name=last_name
            )

            if isinstance(result, str):
                print(result)
            else:
                print(f"Modified: {result[0]} {result[1]}.")

        elif choice == "3":
            phone_number = input("Enter phone number: ").strip()

            try:
                phone_number = int(phone_number)
            except ValueError:
                print("Invalid phone number.")
                continue

            result = contacts.delete_contact(
                contact_list,
                id=phone_number
            )

            if isinstance(result, str):
                print(result)
            else:
                print(f"Deleted: {result[0]} {result[1]}.")

        elif choice == "4":
            contacts.print_list(contact_list)

        elif choice == "5":
            search = input("Enter search string: ").strip()

            found = contacts.find_contact(
                contact_list,
                find=search
            )

            contacts.print_found(found)

        elif choice == "6":
            break

        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()