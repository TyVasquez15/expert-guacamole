# Name: Tyler Vasquez
# Date: 9/14/2026
# Main driver and input program for the employee contact list.

import contacts


def main():
    contact_list = []

    while True:
        print("\n*** EMPLOYEE CONTACT MAIN MENU")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Sort list by first name")
        print("6. Sort list by last name")
        print("7. Exit the program")

        choice = input("Enter menu choice: ").strip()

        if choice == "1":
            contacts.print_list(contact_list)

        elif choice == "2":
            first_name = input("Enter first name: ").strip()
            while not first_name:
                print("Invalid first name.")
                first_name = input("Enter first name: ").strip()

            last_name = input("Enter last name: ").strip()
            while not last_name:
                print("Invalid last name.")
                last_name = input("Enter last name: ").strip()

            contacts.add_contact(
                contact_list,
                first_name=first_name,
                last_name=last_name
            )

        elif choice == "3":
            if len(contact_list) == 0:
                print("Contact list is empty. Add a contact before modifying it.")
                continue

            index_input = input("Enter the index number: ").strip()

            try:
                index = int(index_input)
            except ValueError:
                print("Invalid index number.")
                continue

            first_name = input("Enter first name: ").strip()
            while not first_name:
                print("Invalid first name.")
                first_name = input("Enter first name: ").strip()

            last_name = input("Enter last name: ").strip()
            while not last_name:
                print("Invalid last name.")
                last_name = input("Enter last name: ").strip()

            result = contacts.modify_contact(
                contact_list,
                first_name=first_name,
                last_name=last_name,
                index=index
            )

            if not result:
                print("Invalid index number.")

        elif choice == "4":
            if len(contact_list) == 0:
                print("The contact list is empty.")
                continue

            index_input = input("Enter the index number: ").strip()

            try:
                index = int(index_input)
            except ValueError:
                print("Invalid index number.")
                continue

            result = contacts.delete_contact(
                contact_list,
                index=index
            )

            if not result:
                print("Invalid index number.")

        elif choice == "5":
            contacts.sort_contacts(contact_list, column=0)

        elif choice == "6":
            contacts.sort_contacts(contact_list, column=1)

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main()
