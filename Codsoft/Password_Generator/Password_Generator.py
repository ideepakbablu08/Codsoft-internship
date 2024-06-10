import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive integer for the password length.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2e3f4f")

label = tk.Label(root, text="Enter password length:", font=("Helvetica", 14), bg="#2e3f4f", fg="#ffffff")
label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Generate Password", font=("Helvetica", 14), command=generate_password, bg="#4caf50", fg="#ffffff", activebackground="#388e3c")
button.pack(pady=10)

text_widget = tk.Text(root, height=5, width=40, font=("Helvetica", 14), bg="#1c2833", fg="#f7f9f9")
text_widget.pack(pady=10)



root.mainloop()
