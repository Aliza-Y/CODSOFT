class Contact:
    def __init__(self, name, cell_number, email, address):
        self.name = name
        self.cell_number = cell_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("Contact list: ")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.cell_number}")

    def search_contact(self, keyword):
        keyword = keyword.lower()
        search_results = []
        for contact in self.contacts:
            if keyword in contact.name.lower() or keyword in contact.cell_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, name, new_phone, new_email, new_address):
        name = name.lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                contact.cell_number = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Existing contact updated!")
                return
        print("Contact not found.")

    def remove_contact(self, name):
        name = name.lower()
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name:
                del self.contacts[idx]
                print("Contact removed from contacts list.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book: ")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Search a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Choose your option: ")
        if choice == '1':
            name = input("Name: ")
            phone_number = input("Phone number: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter the name or phone number of the contact you want to search: ")
            search_results = contact_book.search_contact(keyword)
            if search_results:
                print("Results: ")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. Name: {contact.name}, Phone: {contact.cell_number}")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter the name of the contact you want to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact you want to delete: ")
            contact_book.remove_contact(name)

        elif choice == '6':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
