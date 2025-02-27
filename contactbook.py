# Contact management system

# Dictionary to store contacts with the name as the key
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts saved yet.")

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
    if not found:
        print("No contact found with that name or phone number.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Current details:", contacts[name])
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        
        if phone: contacts[name]['Phone'] = phone
        if email: contacts[name]['Email'] = email
        if address: contacts[name]['Address'] = address
        
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"No contact found for {name}.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found for {name}.")

# User interface
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please choose again.")

# Run the program
if __name__ == "__main__":
    main()
