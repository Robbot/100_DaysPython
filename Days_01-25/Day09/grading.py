student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades={}

# Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if 91 <= student_scores[student] < 100:
        student_grades[student] = "Outstanding"
    elif 81 <= student_scores[student] < 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    elif 0 < student_scores[student] < 70:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)





