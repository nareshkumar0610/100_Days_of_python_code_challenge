'''Q: Write a code to identify the highest mark the student scores'''

### Write your code below ###

#Step_1: Ask input from the user

student_marks = input("Give me the marks of the students: ").split()

print(student_marks)

for marks in range(0, len(student_marks)):
    student_marks[marks] = int(student_marks[marks])

print(student_marks)

#Method_1:
student_marks.sort()

print(f"Method_1\nHighest Mark of the student is {student_marks[-1]}")

# Method_2:
value = 0
for mark in student_marks:
    if mark > value:
        value = mark

print(f"Method_2\nHighest mark of the student is {value}")
        



