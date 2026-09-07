from contacts import *

# Name: Tyler Vasquez
# Date: 9/9/2026
# Main driver and input program

def main():
    contacts = []

    while True:
        print("\n*** EMPLOYEE CONTACT MAIN MENU")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Exit the program")

        choice = input("Enter menu choice: ").strip()

        if choice == "1":
            print_list(contacts)

        elif choice == "2":
            contacts = add_contact(contacts)

        elif choice == "3":
            contacts = modify_contact(contacts)

        elif choice == "4":
            contacts = delete_contact(contacts)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main()