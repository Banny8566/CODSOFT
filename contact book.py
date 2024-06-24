import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Manager")
        self.create_widgets()

    def create_widgets(self):
        # Add Contact Button
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)
        
        # View Contacts Button
        self.view_button = tk.Button(self.root, text="View Contact List", command=self.view_contacts)
        self.view_button.pack(pady=10)

        # Search Contacts Button
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=10)

    def add_contact(self):
        store_name = simpledialog.askstring("Input", "Enter Store Name:")
        phone_number = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        
        if store_name and phone_number and email and address:
            new_contact = Contact(store_name, phone_number, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact Added Successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def view_contacts(self):
        contact_list_window = tk.Toplevel(self.root)
        contact_list_window.title("Contact List")
        
        for contact in self.contacts:
            contact_details = f"Name: {contact.store_name}, Phone: {contact.phone_number}"
            tk.Label(contact_list_window, text=contact_details).pack()

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        
        if search_term:
            search_results = [contact for contact in self.contacts if search_term.lower() in contact.store_name.lower() or search_term in contact.phone_number]
            
            if search_results:
                search_result_window = tk.Toplevel(self.root)
                search_result_window.title("Search Results")
                
                for contact in search_results:
                    contact_details = f"Name: {contact.store_name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}"
                    tk.Label(search_result_window, text=contact_details).pack()
            else:
                messagebox.showinfo("No Results", "No contacts found matching the search term.")
        else:
            messagebox.showwarning("Input Error", "Search term is required!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
