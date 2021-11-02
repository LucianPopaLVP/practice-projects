student_scores = {
    'Lucian': 74,
    'Adina': 93,
    'Mihaela': 87,
    'Sara': 99,
    'Vasile': 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding!"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations!"
    elif score > 70:
        student_grades[student] = "Accetable!"
    else:
        student_grades[student] = "Fail!"

print(student_grades)

