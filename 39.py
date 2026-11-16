# Write mode
f = open("student.txt", "w")
f.write("Welcome to Python\n")
f.close()

# Append mode
f = open("student.txt", "a")
f.write("File Handling Example\n")
f.close()

# Read mode
f = open("student.txt", "r")
print(f.read())
f.close()

# Read and write mode
f = open("student.txt", "r+")
print("File content:")
print(f.read())
f.close()
