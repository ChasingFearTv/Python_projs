student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highScore = 0
for num in student_scores:
    if num > highScore:
        highScore = num
print(f"The highest score in the class is: {highScore}")