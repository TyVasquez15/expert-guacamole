
# Name: Tyler Vasquez
# Date: 10/22/2026
# Provides a class for managing a saved Tuffy Titan contact list.

import json


class Contacts:
    """Manage contacts stored in a JSON file."""

    def __init__(self, *, filename="contacts.json"):
        """Initialize contacts by loading the specified JSON file."""
        self.filename = filename
        self.data = {}

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_contacts(self):
        """Save the contact dictionary to the JSON file."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def sort_contacts(self):
        """Sort contacts by last name and then first name."""
        self.data = dict(
            sorted(
                self.data.items(),
                key=lambda item: (
                    item[1][1].lower(),
                    item[1][0].lower()
                )
            )
        )

    def add_contact(self, *, id, first_name, last_name):
        """Add a contact unless its phone number already exists."""
        if id in self.data:
            return "error2"

        self.data[id] = [first_name, last_name]
        self.sort_contacts()
        self.save_contacts()
        return {id: self.data[id]}

    def modify_contact(self, *, id, first_name, last_name):
        """Modify an existing contact."""
        if id not in self.data:
            return "error"

        self.data[id] = [first_name, last_name]
        self.sort_contacts()
        self.save_contacts()
        return {id: self.data[id]}

    def delete_contact(self, *, id):
        """Delete an existing contact and return its information."""
        if id not in self.data:
            return "error"

        deleted_contact = {id: self.data.pop(id)}
        self.save_contacts()
        return deleted_contact

    def set_filename(self, *, filename):
        """Change the file used to load and save contacts."""
        self.filename = filename
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
