import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from backend import db_connect


conn = db_connect.connect_db()
cursor = conn.cursor()


window = tk.Tk()
window.title("Manage Rooms")


tree = ttk.Treeview(window, columns=("ID", "Room Number", "Room Type", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Room Number", text="Room Number")
tree.heading("Room Type", text="Room Type")
tree.heading("Status", text="Status")
tree.pack(pady=10)

def load_rooms():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM rooms")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


tk.Label(window, text="Room Number").pack(pady=5)
entry_room_no = tk.Entry(window)
entry_room_no.pack(pady=5)

tk.Label(window, text="Room Type").pack(pady=5)
entry_room_type = tk.Entry(window)
entry_room_type.pack(pady=5)

tk.Label(window, text="Status").pack(pady=5)
entry_status = tk.Entry(window)
entry_status.pack(pady=5)


selected_room_id = None  
def on_room_select(event):
    global selected_room_id
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")
        selected_room_id = values[0]
        entry_room_no.delete(0, tk.END)
        entry_room_no.insert(0, values[1])
        entry_room_type.delete(0, tk.END)
        entry_room_type.insert(0, values[2])
        entry_status.delete(0, tk.END)
        entry_status.insert(0, values[3])


def update_room():
    global selected_room_id
    if selected_room_id:
        room_no = entry_room_no.get()
        room_type = entry_room_type.get()
        status = entry_status.get()
        try:
            cursor.execute(
                "UPDATE rooms SET room_number=%s, room_type=%s, status=%s WHERE id=%s",
                (room_no, room_type, status, selected_room_id)
            )
            conn.commit()
            messagebox.showinfo("Success", "Room updated successfully!")
            load_rooms()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No room selected.")


def delete_room():
    global selected_room_id
    if selected_room_id:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this room?")
        if confirm:
            try:
                cursor.execute("DELETE FROM rooms WHERE id=%s", (selected_room_id,))
                conn.commit()
                messagebox.showinfo("Deleted", "Room deleted successfully!")
                load_rooms()
                entry_room_no.delete(0, tk.END)
                entry_room_type.delete(0, tk.END)
                entry_status.delete(0, tk.END)
                selected_room_id = None
            except Exception as e:
                messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Warning", "No room selected.")



tree.bind("<<TreeviewSelect>>", on_room_select)


btn_refresh = tk.Button(window, text="Refresh", command=load_rooms)
btn_refresh.pack(pady=5)

btn_update = tk.Button(window, text="Update Room", command=update_room)
btn_update.pack(pady=5)

btn_delete = tk.Button(window, text="Delete Room", command=delete_room)
btn_delete.pack(pady=5)



load_rooms()

window.mainloop()
