import sqlite3

# Connect to database
con = sqlite3.connect("student.db")

# Create cursor
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert records
cur.execute("INSERT INTO students VALUES (1, 'Rahul', 85)")
cur.execute("INSERT INTO students VALUES (2, 'Amit', 90)")
cur.execute("INSERT INTO students VALUES (3, 'Priya', 78)")

# Display records
cur.execute("SELECT * FROM students")

data = cur.fetchall()

for row in data:
    print(row)

# Save changes
con.commit()

# Close connection
con.close()
