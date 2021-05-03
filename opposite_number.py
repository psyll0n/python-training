# Given a number, find its opposite.
print("Enter a number to get its opposite as a result.")

try: 
    number = int(input("Enter a number: "))

    def oppositeNumber(number):
        return -1 * number


    print(oppositeNumber(number))
except: 
    print("You did not enter a number.")