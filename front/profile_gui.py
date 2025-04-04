import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="759196",  
    database="hotel_db"
)
cursor = conn.cursor()

def update_profile():
    new_name = entry_name.get()
    new_email = entry_email.get()
    new_password = entry_password.get()

    if new_name and new_email and new_password:
        query = "UPDATE profile SET name=%s, email=%s, password=%s WHERE admin_id=1"
        cursor.execute(query, (new_name, new_email, new_password))
        conn.commit()
        messagebox.showinfo("Success", "Profile updated successfully!")
    else:
        messagebox.showwarning("Warning", "All fields are required!")

def sign_out(window):
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to sign out?")
    if confirm:
        window.destroy()  # Close the current window
        import login_gui  # Redirect to login page
        login_gui.main()  # Assuming you have a login page setup


root = tk.Tk()
root.title("Profile Management")
root.geometry("300x200")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_update = tk.Button(root, text="Update Profile", command=update_profile)
btn_update.pack(pady=10)

root.mainloop()
