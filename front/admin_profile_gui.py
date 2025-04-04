import tkinter as tk
from tkinter import messagebox
import mysql.connector

def load_profile():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, email, username FROM users WHERE username = 'admin'")
        result = cursor.fetchone()
        conn.close()

        if result:
            entry_name.delete(0, tk.END)
            entry_name.insert(0, result[0])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, result[1])
            entry_username.delete(0, tk.END)
            entry_username.insert(0, result[2])
        else:
            messagebox.showerror("Error", "Admin profile not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_profile():
    name = entry_name.get()
    email = entry_email.get()

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE username='admin'", (name, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Profile updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Admin Profile")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root, state="readonly")
entry_username.pack()

tk.Button(root, text="Update Profile", command=update_profile).pack(pady=10)

load_profile()
root.mainloop()
