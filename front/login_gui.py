import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to authenticate user
def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_db")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", "Welcome, " + username)
            root.destroy()
            import manage_rooms  # Redirect to main dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))


def sign_out(window):
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to sign out?")
    if confirm:
        window.destroy()
        import login_gui


# Create Login Window
root = tk.Tk()
root.title("Hotel Management - Login")

tk.Label(root, text="Username:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Login", command=authenticate)
btn_login.pack()

root.mainloop()
