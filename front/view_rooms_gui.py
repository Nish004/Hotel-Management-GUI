import tkinter as tk
from tkinter import ttk
from backend import db_connect

def fetch_rooms():
    conn = db_connect.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    rows = cursor.fetchall()
    conn.close()
    return rows

def show_rooms():
    data = fetch_rooms()

    window = tk.Tk()
    window.title("Room List")
    window.geometry("600x400")

 
    tree = ttk.Treeview(window, columns=("ID", "Room Number", "Room Type", "Status"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Room Number", text="Room Number")
    tree.heading("Room Type", text="Room Type")
    tree.heading("Status", text="Status")

    for row in data:
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True)
    window.mainloop()

if __name__ == "__main__":
    show_rooms()
