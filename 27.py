'''Write a program to copy move and delete files
using shutil module'''

import shutil
import os

# Create a file
with open("source.txt", "w") as f:
    f.write("Hello Python")

# Copy file
shutil.copy("source.txt", "copy.txt")
print("File copied.")

# Move file
shutil.move("copy.txt", "moved.txt")
print("File moved.")

# Delete file
os.remove("moved.txt")
print("File deleted.")
