# Name: Tyler Vasquez
# Date: 9/14/2026
# Provides functions for managing an employee contact list.

def print_list(contacts):
    print("================== CONTACT LIST ==================")
    print(f'{"Index":8}{"First Name":22}{"Last Name":22}')
    print(f'{"======":8}{"====================":22}{"====================":22}')

    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

    input("\nPress enter to continue.")


def add_contact(contacts, *, first_name, last_name):
    """Add a new contact to the contact list."""
    contacts.append([first_name, last_name])


def modify_contact(contacts, *, first_name, last_name, index):
    if 0 <= index < len(contacts):
        contacts[index] = [first_name, last_name]
        return True

    return False


def delete_contact(contacts, *, index):
    if 0 <= index < len(contacts):
        del contacts[index]
        return True

    return False


def sort_contacts(contacts, *, column):
    if column == 0:
        contacts.sort(key=lambda contact: contact[0])
    elif column == 1:
        contacts.sort(key=lambda contact: contact[1])
