import random

# Create a dictionary by using the values in a the list `names`
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Conditional dictionary comprehension
passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 60
}
print(passed_students)

# The example below creates a dictionary called result that takes each word in the given sentence and calculates
# the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words_list = sentence.split()

print(words_list)


result = {word: len(word) for word in words_list}

print(result)

#  The dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula: `(temp_c * 9 / 5) + 32 = temp_f`

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

temp_f = {k: (v * 9 / 5) + 32 for (k, v) in weather_c.items()}

print(temp_f)

weather_f = {key: value for (key, value) in temp_f.items()}

print(weather_f)
