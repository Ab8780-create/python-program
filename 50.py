import sqlite3

# Connect to database
con = sqlite3.connect("student.db")

cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

# Clear old records for repeatable output
cur.execute("DELETE FROM students")

# Insert records
students = [
    (1, 'Rahul', 85),
    (2, 'Amit', 90),
    (3, 'Priya', 78),
    (4, 'Neha', 95),
    (5, 'Raj', 88)
]

cur.executemany(
    "INSERT INTO students VALUES (?, ?, ?)",
    students
)

con.commit()

# Fetch one record
cur.execute("SELECT * FROM students")
print("Fetch One:")
print(cur.fetchone())

# Fetch multiple records
cur.execute("SELECT * FROM students")
print("\nFetch Many:")
print(cur.fetchmany(3))

# Fetch all records
cur.execute("SELECT * FROM students")
print("\nFetch All:")
print(cur.fetchall())

con.close()
