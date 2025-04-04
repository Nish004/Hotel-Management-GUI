import tkinter as tk
from tkinter import messagebox
from backend import db_connect

def add_room():
    room_number = entry_room_number.get()
    room_type = entry_room_type.get()
    status = entry_status.get()

    if not room_number or not room_type or not status:
        messagebox.showerror("Error", "All fields are required.")
        return

    conn = db_connect.connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO rooms (room_number, room_type, status) VALUES (%s, %s, %s)",
                       (room_number, room_type, status))
        conn.commit()
        messagebox.showinfo("Success", "Room added successfully!")
        entry_room_number.delete(0, tk.END)
        entry_room_type.delete(0, tk.END)
        entry_status.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add room: {e}")
    finally:
        conn.close()


window = tk.Tk()
window.title("Add New Room")
window.geometry("400x300")

tk.Label(window, text="Room Number").pack(pady=5)
entry_room_number = tk.Entry(window)
entry_room_number.pack(pady=5)

tk.Label(window, text="Room Type").pack(pady=5)
entry_room_type = tk.Entry(window)
entry_room_type.pack(pady=5)

tk.Label(window, text="Status (Available / Occupied)").pack(pady=5)
entry_status = tk.Entry(window)
entry_status.pack(pady=5)

tk.Button(window, text="Add Room", command=add_room).pack(pady=20)

window.mainloop()
