import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, search_name):
        matching_contacts = [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]
        if not matching_contacts:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for contact in matching_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def update_contact(self, search_name, new_name, new_phone, new_email):
        matching_contacts = [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]
        if not matching_contacts:
            print("Contact not found.")
        else:
            for contact in matching_contacts:
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
            print("Contact updated successfully!")

    def delete_contact(self, search_name):
        matching_contacts = [contact for contact in self.contacts if search_name.lower() in contact.name.lower()]
        if not matching_contacts:
            print("Contact not found.")
        else:
            for contact in matching_contacts:
                self.contacts.remove(contact)
            print("Contact deleted successfully!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            clear_screen()
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address_book.add_contact(name, phone, email)

        elif choice == "2":
            clear_screen()
            address_book.view_contacts()

        elif choice == "3":
            clear_screen()
            search_name = input("Enter a name to search: ")
            address_book.search_contact(search_name)

        elif choice == "4":
            clear_screen()
            search_name = input("Enter a name to update: ")
            new_name = input("Enter new contact name: ")
            new_phone = input("Enter new contact phone: ")
            new_email = input("Enter new contact email: ")
            address_book.update_contact(search_name, new_name, new_phone, new_email)

        elif choice == "5":
            clear_screen()
            search_name = input("Enter a name to delete: ")
            address_book.delete_contact(search_name)

        elif choice == "6":
            clear_screen()
            print("Goodbye!")
            break

        else:
            clear_screen()
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
