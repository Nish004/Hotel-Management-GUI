import tkinter as tk
from tkinter import messagebox
import subprocess

root = tk.Tk()
root.title("Hotel Management Dashboard")
root.geometry("300x400")

def open_manage_rooms():
    subprocess.Popen(["python", "front/manage_rooms_gui.py"])

def open_customers():
    subprocess.Popen(["python", "front/add_customer_gui.py"])

def open_checkout():
    subprocess.Popen(["python", "front/checkout_gui.py"])

def open_billing_history():
    subprocess.Popen(["python", "front/view_bills_gui.py"])

def open_profile():
    subprocess.Popen(["python", "front/profile_gui.py"])

tk.Label(root, text="Welcome to Hotel Manager", font=("Helvetica", 14, "bold")).pack(pady=15)

tk.Button(root, text="Manage Rooms", width=25, command=open_manage_rooms).pack(pady=5)
tk.Button(root, text="Customers", width=25, command=open_customers).pack(pady=5)
tk.Button(root, text="Check-Out", width=25, command=open_checkout).pack(pady=5)
tk.Button(root, text="Billing History", width=25, command=open_billing_history).pack(pady=5)
tk.Button(root, text="Admin Profile", width=25, command=open_profile).pack(pady=5)

tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()
