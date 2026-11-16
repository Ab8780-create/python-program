"""25.Write a program to display current date and
time using datetime module.
"""
from datetime import datetime

now = datetime.now()

print("Current Date and Time:", now)
print("Date:", now.date())
print("Time:", now.time())
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)