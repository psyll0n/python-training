# Import the My_Calc class defined in using_methods_example.py

from using_methods_example import My_Calc

calc1 = My_Calc(1000, 200)
total1 = calc1.total()
diff1 = calc1.diff()
print("Total1: ", total1)
print("Diff1: ", diff1)

print("-----------------")
calc2 = My_Calc(523, 235)
total2 = calc2.total()
diff2 = calc2.diff()
print("Total2: ", total2)
print("Diff2: ", diff2)
