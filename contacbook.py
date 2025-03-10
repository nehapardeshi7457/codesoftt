import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        self.label = tk.Label(root, text="Contact Book", font=("Arial", 16))
        self.label.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()
    
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
    
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts available.")
            return
        contact_list = "\n".join([f"{name}: {info['Phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)
    
    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter name or phone number:")
        for name, info in self.contacts.items():
            if search_query in [name, info['Phone']]:
                contact_details = f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}"
                messagebox.showinfo("Contact Found", contact_details)
                return
        messagebox.showerror("Not Found", "Contact not found.")
    
    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[name]['Phone'])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=self.contacts[name]['Email'])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=self.contacts[name]['Address'])
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")
    
    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
