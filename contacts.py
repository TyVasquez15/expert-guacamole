# Name: Tyler Vasquez
# Date: 9/20/2026
# Provides functions for managing an employee contact list.

def add_contact(contacts, *, id, first_name, last_name):
    # Add a new contact to the contact dictionary.
    if id in contacts:
        return "Phone number already exists."

    contacts[id] = [first_name, last_name]
    return contacts[id]

def modify_contact(contacts, *, id, first_name, last_name):
    # Modify an existing contact in the contact dictionary.
    if id not in contacts:
        return "Phone number does not exist."

    contacts[id] = [first_name, last_name]
    return contacts[id]


def delete_contact(contacts, *, id):
    # Delete a contact from the contact dictionary.
    if id not in contacts:
        return "Invalid phone number."

    return contacts.pop(id)

def sort_contacts(contacts):
    # Return contacts sorted by last name and then first name.
    return dict(
        sorted(
            contacts.items(),
            key=lambda item: (item[1][1].lower(), item[1][0].lower())
        )
    )

def find_contact(contacts, *, find):
    # Find contacts by phone number, first name, or last name.
    found = {}

    if find.isnumeric():
        phone_number = int(find)

        if phone_number in contacts:
            found[phone_number] = contacts[phone_number]

    search_text = find.lower()

    for id, name in contacts.items():
        first_name = name[0]
        last_name = name[1]

        if search_text in first_name.lower() or search_text in last_name.lower():
            found[id] = name

    return sort_contacts(found)

def print_list(contacts):
    # Print the contacts in sorted order.
    sorted_contacts = sort_contacts(contacts)

    print("==================== CONTACT LIST ====================")
    print("Last Name           First Name          Phone")
    print("==================== ==================== ==========")

    for id, name in sorted_contacts.items():
        print(f"{name[1]:20}{name[0]:20}{id}")

def print_found(contacts):
    # Print contacts.
    print("================== FOUND CONTACT(S) ==================")
    print("Last Name           First Name          Phone")
    print("==================== ==================== ==========")


    for id, name in contacts.items():
        print(f"{name[1]:20}{name[0]:20}{id}")

