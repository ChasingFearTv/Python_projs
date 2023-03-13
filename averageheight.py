# average height without using len and sum
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
amount = 0
for student in student_heights:
    total += student
for student in student_heights:
    amount += 1
average = round(total / amount)

print(average)
