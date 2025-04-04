import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend import db_connect


conn = db_connect.connect_db()

cursor = conn.cursor()

cursor.execute("SELECT * FROM rooms")
rows = cursor.fetchall()

print("Room Data:")
for row in rows:
    print(row)

conn.close()
