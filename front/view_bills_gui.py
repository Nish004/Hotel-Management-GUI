import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_bills():
    tree.delete(*tree.get_children())  # Clear table
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

root = tk.Tk()
root.title("Billing History")

tree = ttk.Treeview(root, columns=("ID", "Customer", "Room", "Check-in", "Check-out", "Days", "Total"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Customer", text="Customer Name")
tree.heading("Room", text="Room No.")
tree.heading("Check-in", text="Check-in")
tree.heading("Check-out", text="Check-out")
tree.heading("Days", text="Days Stayed")
tree.heading("Total", text="Total Amount")
tree.pack(padx=10, pady=10)

btn = tk.Button(root, text="Refresh", command=fetch_bills)
btn.pack(pady=5)

fetch_bills()
root.mainloop()
