#!/bin/env/python3
# birthday_paradox_sim.py - The script explores the surprising probabilities of the "Birthday Paradox".

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for the current simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a data that occurs more than once in the 
    birthdays list."""
    if (len(birthdays)) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print(
    """A script that demonstrates the so-called 'Birthday Paradox'.
      The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large. This program 
does a Monte Carlo simulation (that is, repeated random simulations) to explore
this concept.

(It's not actually a paradox, it's just a surprising result.)
"""
)

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True:  # Keep asking until the user enter a valid amount.
    print("How many birthdays should I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")
    monthName = MONTHS[birthday.month - 1]
    dateText = "{} {}".format(monthName, birthday.day)
    print(dateText, end="")
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print("In this simulation, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("Multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()

# Run 100,000 simulations:
print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press enter to begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0  # How many simulations had maching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run.")

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people, there was a")
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays, "people have a", probability, "% chance of")
print("having a matching birthday in their group.")
print("That's probably more than you would think!")
