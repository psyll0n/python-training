"""BMI Calculator with Health Classification.

Calculates Body Mass Index (BMI) from height and weight inputs and provides
health classification based on standard BMI ranges.

BMI Formula: BMI = weight (kg) / height² (m²)

BMI Categories:
- Below 18.5: Underweight
- 18.5 - 24.9: Normal weight
- 25.0 - 29.9: Slightly overweight
- 30.0 - 34.9: Obese
- 35.0 and above: Clinically obese

Features:
- User input validation
- BMI calculation
- Health classification
- Error handling for invalid inputs
"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Calculate BMI and round to nearest integer
bmi = round(weight / (height * height))

try:
    if bmi == 0:
        print("Your bmi was not calculated correctly due to wrong input values.")
    # Under 18.5 they are underweight
    elif bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight.")
    # Over 18.5 but below 25 they have a normal weight
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight.")
    # Over 25 but below 30 they are slightly overweight
    elif bmi < 30:
        print(f"Your bmi is {bmi}, you are slightly overweight.")
    # Over 30 but below 35 they are obese
    elif bmi < 35:
        print(f"Your bmi is {bmi}, you are obese.")
    # Above 35 they are clinically obese
    else:
        print(f"Your bmi is {bmi}, you are clinically obese.")
except:
    print("You have not entered your height and weight correctly")
