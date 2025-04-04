import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="759196",
        database="hotel_db"
    )


def add_customer():
    name = entry_name.get()
    phone = entry_phone.get()
    id_proof = entry_id.get()
    
    if name == "" or phone == "" or id_proof == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO customers (name, phone, id_proof) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, phone, id_proof))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Customer Added Successfully")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    load_customers()


def load_customers():
    for row in customer_table.get_children():
        customer_table.delete(row)
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        customer_table.insert("", tk.END, values=row)


root = tk.Tk()
root.title("Customer Management")
root.geometry("600x400")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="ID Proof:").grid(row=2, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=2, column=1, padx=10, pady=5)


btn_add = tk.Button(root, text="Add Customer", command=add_customer)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)


columns = ("ID", "Name", "Phone", "ID Proof")
customer_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    customer_table.heading(col, text=col)
    customer_table.column(col, width=100)

customer_table.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
load_customers()


root.mainloop()