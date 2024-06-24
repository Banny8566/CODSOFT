import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    
    character_set = ''
    if var_uppercase.get():
        character_set += string.ascii_uppercase
    if var_lowercase.get():
        character_set += string.ascii_lowercase
    if var_digits.get():
        character_set += string.digits
    if var_symbols.get():
        character_set += string.punctuation
    
    if not character_set:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    result_label.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Character type checkboxes
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=var_uppercase)
uppercase_check.pack()

lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=var_lowercase)
lowercase_check.pack()

digits_check = tk.Checkbutton(root, text="Include Digits", variable=var_digits)
digits_check.pack()

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols)
symbols_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
