# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

#Write your code below this row 👇
student_height_total = 0
student_number = 0

for student in student_heights:
    student_height_total += student
    student_number += 1
average_height = round(student_height_total/student_number)
print(f"The average height of student is {average_height}")
