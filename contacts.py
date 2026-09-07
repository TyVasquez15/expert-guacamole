# Name: Tyler Vasquez
# Date: 9/9/2026
# Provides functions for managing an employee contact list.

def print_list(contacts):
    print("================== CONTACT LIST ==================")
    print(f'{"Index":8}{"First Name":22}{"Last Name":22}')
    print(f'{"======":8}{"====================":22}{"====================":22}')

    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

    input("\nPress enter to continue.")

def add_contact(contacts):
    first_name = input("Enter First Name: ").strip()
    while not first_name:
        print("Invalid first name.")
        first_name = input("Enter first name: ").strip()

    last_name = input("Enter last name: ").strip()
    while not last_name:
        print("Invalid last name.")
        last_name = input("Enter last name: ").strip()

    contacts.append([first_name, last_name])
    return contacts

def modify_contact(contacts):
    if len(contacts) == 0:
        print("Contact list is empty. Add a contact before modifying it.")
        input("\nPress enter to continue.")
        return contacts

    index_input = input("Enter the index number: ").strip()

    try:
        index = int(index_input)
    except ValueError:
        print("Invalid index number.")
        return contacts

    if index < 0 or index >= len(contacts):
        print("Invalid index number.")
        return contacts

    first_name = input("Enter first name: ").strip()
    while not first_name:
        print("Invalid first name.")
        first_name = input("Enter first name: ").strip()

    last_name = input("Enter last name: ").strip()
    while not last_name:
        print("Invalid last name.")
        last_name = input("Enter last name: ").strip()

    contacts[index] = [first_name, last_name]
    return contacts

def delete_contact(contacts):
    if len(contacts) == 0:
        print("The contact list is empty.")
        return contacts

    index_input = input("Enter the index number: ").strip()

    try:
        index = int(index_input)
    except ValueError:
        print("Invalid index number.")
        return contacts

    if index < 0 or index >= len(contacts):
        print("Invalid index number.")
        return contacts

    del contacts[index]
    return contacts

