import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Contact Book")

# Data structure to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if name and phone and email:
        contacts[name] = {'phone': phone, 'email': email}
        update_contact_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to update the contact list display
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

# Function to show contact details
def show_contact_details(event):
    selected_contact = listbox_contacts.get(listbox_contacts.curselection())
    contact_details = contacts[selected_contact]
    messagebox.showinfo("Contact Details", f"Name: {selected_contact}\nPhone: {contact_details['phone']}\nEmail: {contact_details['email']}")

# Labels and entry fields for contact details
label_name = tk.Label(root, text="Name:")
label_phone = tk.Label(root, text="Phone:")
label_email = tk.Label(root, text="Email:")

entry_name = tk.Entry(root, width=30)
entry_phone = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)

# Button to add contact
button_add = tk.Button(root, text="Add Contact", command=add_contact)

# Listbox to display contacts
listbox_contacts = tk.Listbox(root, width=50, height=15)
listbox_contacts.bind('<<ListboxSelect>>', show_contact_details)

# Layout using grid
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name.grid(row=0, column=1, padx=10, pady=5)
label_phone.grid(row=1, column=0, padx=10, pady=5)
entry_phone.grid(row=1, column=1, padx=10, pady=5)
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email.grid(row=2, column=1, padx=10, pady=5)
button_add.grid(row=3, columnspan=2, pady=10)
listbox_contacts.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
