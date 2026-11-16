f = open("student.txt", "w")
f.write("Python Programming")
f.close()

f = open("student.txt", "r")

# Current file pointer position
print("Initial position:", f.tell())

# Read first 6 characters
print("Data:", f.read(6))

# Current position
print("Current position:", f.tell())

# Move pointer to position 7
f.seek(7)

# Read remaining data
print("Remaining data:", f.read())

# Close file
f.close()
