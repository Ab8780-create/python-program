'''26. Write a program to perform file and directory
operations using os and sys modules.'''


import os
import sys

# Current directory
print("Current Directory:", os.getcwd())

# List files and folders
print("Files and Folders:")
print(os.listdir())

# Create directory
if not os.path.exists("TestFolder"):
    os.mkdir("TestFolder")
    print("Directory created.")

# Check directory
print("Directory exists:", os.path.exists("TestFolder"))

# Python version using sys
print("Python Version:", sys.version)

# Operating system
print("Operating System:", os.name)
