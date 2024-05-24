'''Q: Write a code to calculate the average height of the students from a list of students'''

### Write a code below ###

#Step_1: Ask user to add list of students height
student_heights = input("Input a list of student heights ").split()

print(f"Height of the students: {student_heights}")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(f"Height of the students: {student_heights}")

#Step_2: Applying formula code for calculating average parameters
count = 0
for counts in student_heights:
    count += 1
print(f"Total number of students is: {count}" )

sum = 0
for sums in student_heights:
    sum += sums
print(f"Sum of height is: {sum}")

Average = round(sum/count)

print(f"Average height is: {Average}")

#####--------------END--------------#####