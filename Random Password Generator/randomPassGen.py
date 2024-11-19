import random
import string
import tkinter as tk
from tkinter import messagebox, font

def generate_password(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits

    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True

        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number

        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd

def on_generate():
    try:
        min_length = int(entry_min_length.get())
        has_number = var_numbers.get()
        has_special = var_special.get()

        password = generate_password(min_length, has_number, has_special)
        label_result.config(text=f"Generated Password: {password}")

        btn_copy.config(state="normal")
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid minimum length.")

def copy_to_clipboard():
    password = label_result.cget("text").replace("Generated Password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
root.configure(bg="#f0f0f5")

label_font = font.Font(family="Helvicta", size=10)
result_font = font.Font(family="Helvicta", size=10, slant="italic")
button_font = font.Font(family="Helvicta", size=10)

label_min_length = tk.Label(root, text="Minimum Length:", font=label_font, bg="#f0f0f5", fg="#333333")
label_min_length.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_min_length = tk.Entry(root, width=10, font=label_font)
entry_min_length.grid(row=0, column=1, padx=10, pady=10, sticky="w")

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, font=label_font, bg="#f0f0f5", fg="#333333", activebackground="#e0e0eb")
check_numbers.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=label_font, bg="#f0f0f5", fg="#333333", activebackground="#e0e0eb")
check_special.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

button_generate = tk.Button(root, text="Generate Password", font=button_font, bg="#4CAF50", fg="white", command=on_generate, relief="raised")
button_generate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Generated Password: ", font=result_font, bg="#f0f0f5", fg="#005580", wraplength=250, justify="center")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

btn_copy = tk.Button(root, text="Copy Password", font=button_font, bg="#2196F3", fg="white", command=copy_to_clipboard, state="disabled")
btn_copy.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()