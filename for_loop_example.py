
# Define a tuple with colours

colours = ('Orange', 'Green', 'Yellow', 'Blue', 'Red', 'Purple')

# Loop through the coulours in the tuple use 'continue' to continue the looping. 

print("Starting the loop...")
for colour in colours:
	if colour == 'Orange':
		continue
	print(colour)
print("Loop has ended.")


# Define a second tuple with colours.    

colours2 = ('Orange', 'Green', 'Yellow', 'Blue', 'Red', 'Purple')

# Loop through the colours in the tuple. 'break' interrupts the looping process. 

print("Starting the loop...")
for colour in colours2:
        if colour == 'Blue':
                break 
        print(colour)
print("Loop has ended.")


# for loop shorthand syntax

print("for loop shorthand")
[print(x) for x in colours]
