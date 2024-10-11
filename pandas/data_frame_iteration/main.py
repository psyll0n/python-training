import pandas

student_data = {
    "student": ["Angela", "James", "John", "Lily", "Andrew"],
    "score": [55, 78, 98, 56, 66]
}

# Loop through a dictionary with a for loop
for key, value in student_data.items():
    print(key)
    print(value)

# Create a Pandas data frame out of the dictionary `student_data`
student_data_frame = pandas.DataFrame(student_data)
print(student_data_frame)

# Loop through the data frame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through the rows of the data frame
for (index, row) in student_data_frame.iterrows():
    # print(index) # Get the indexes of all the rows in the data frame
    # print(row) # Each row represents a Pandas series
    # print(row.student)
    if row.student == "Angela":
        print(row.score) # Access the score of the student "Angela"