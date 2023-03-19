#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

sumToPay=0

totalBill=int((input("What was the total bill? $")))

tipPercentage=int((input("What percentage tip would you like to give? 10, 12, or 15 ")))

numberOfPeople=int((input("How many people to split the bill? ")))

if tipPercentage == 10:
    sumToPay=(totalBill * 1.1)
elif tipPercentage == 12:
    sumToPay=(totalBill * 1.12)
else:
    sumToPay=(totalBill * 1.15)
    
print("Each person should pay: $", round(sumToPay, 2))