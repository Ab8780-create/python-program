import matplotlib.pyplot as plt

# Data
subjects = ['Python', 'Java', 'SQL', 'C++']
marks = [85, 90, 75, 80]

# 1. Line Chart
plt.plot(subjects, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Histogram
plt.hist(marks, bins=4)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Pie Chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
