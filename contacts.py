Name: Tyler Vasquez
Date: 9/16/2026
Provides functions for managing an employee contact list.

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
# Delete an existing contact from the contact dictionary.
if id not in contacts:
return "Invalid phone number."

deleted_contact = contacts.pop(id)
return deleted_contact

def sort_contacts(contacts):
# Sort contacts by last name and then first name.
sorted_contacts = dict(
sorted(
contacts.items(),
key=lambda contact: (contact[1][1], contact[1][0])
)
)

return sorted_contacts

def find_contact(contacts, *, find):
# Find contacts by phone number, first name, or last name.
found_contacts = {}

if find in contacts:
    found_contacts[find] = contacts[find]

for id, contact in contacts.items():
    if find.lower() in contact[0].lower() or find.lower() in contact[1].lower():
        found_contacts[id] = contact

found_contacts = dict(
    sorted(
        found_contacts.items(),
        key=lambda contact: (contact[1][1], contact[1][0])
    )
)

return found_contacts