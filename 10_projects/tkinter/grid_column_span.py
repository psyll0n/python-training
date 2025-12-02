"""Tkinter Grid Layout - Column Span Demonstration.

Demonstrates the use of columnspan in tkinter's grid layout manager.
Shows how to make widgets span multiple columns for flexible layouts.

Features:
- Grid layout with 3 colored labels
- Columnspan usage to make a widget span 2 columns
- Custom widget sizing (width and height)
"""

from tkinter import *

# Create main window
window = Tk()

# Red label in top-left (row 0, column 0)
r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

# Green label in middle (row 1, column 1)
g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

# Blue label at bottom spanning 2 columns (row 2, columns 0-1)
b = Label(bg="blue", width=40, height=5)
b.grid(row=2, column=0, columnspan=2)  # Spans both columns

# Start the main event loop
window.mainloop()
