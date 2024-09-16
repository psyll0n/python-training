#! python3 

"""
This is the scoring criteria: 

    - Scores 91 - 100: Grade = "Outstanding" 

    - Scores 81 - 90: Grade = "Exceeds Expectations" 

    - Scores 71 - 80: Grade = "Acceptable" 

    - Scores 70 or lower: Grade = "Fail" 
"""


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}

# The loop below iterates through the keys and values in the student_grades
# dictionary and asseses the grade (value) of each student (key).
for student, score in student_scores.items():
    if score >= 91:
        student_grades.update({student: "Outstanding"})
    elif score >= 81:
        student_grades.update({student: "Exceeds Expectations"})
    elif score >= 71:
        student_grades.update({student: "Acceptable"})
    else:
        student_grades.update({student: "Fail"})


print(student_grades)
