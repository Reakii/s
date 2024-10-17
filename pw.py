import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength():
    password = password_entry.get()

    if len(password) == 0:
        messagebox.showerror("Error", "Password field cannot be empty.")
    elif len(password) < 6:
        strength_label.config(text="Weak Password", fg="red")
    elif 6 <= len(password) < 10:
        strength_label.config(text="Moderate Password", fg="orange")
    else:
        strength_label.config(text="Strong Password", fg="green")

# Create the main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create and place input fields and labels
tk.Label(window, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(window, show='*')  # Hide input using 'show' parameter
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to check the password strength
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display the password strength
strength_label = tk.Label(window, text="")
strength_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
