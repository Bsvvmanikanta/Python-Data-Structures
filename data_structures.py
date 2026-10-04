# Python Data Structures Practice
# This program demonstrates lists, dictionaries, sets, and tuples.

# List of student names
students = ["Rahul", "Priya", "Arjun", "Sneha"]

# Dictionary containing student marks
marks = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 88
}

# Set containing unique courses
courses = {"Python", "Java", "Python", "SQL"}

# Tuple containing fixed student details
student_details = ("Rahul", 21, "Computer Science")


print("===== Python Data Structures =====")

# Display the list
print("\nStudent List:")
for student in students:
    print("-", student)

# Display the dictionary
print("\nStudent Marks:")
for name, mark in marks.items():
    print(name, ":", mark)

# Display the set
print("\nUnique Courses:")
for course in courses:
    print("-", course)

# Display the tuple
print("\nStudent Details:")
print("Name:", student_details[0])
print("Age:", student_details[1])
print("Course:", student_details[2])

# Calculate the average mark
average = sum(marks.values()) / len(marks)

print("\nAverage Mark:", average)

# Find students who scored 80 or above
print("\nStudents scoring 80 or above:")

for name, mark in marks.items():
    if mark >= 80:
        print("-", name)
