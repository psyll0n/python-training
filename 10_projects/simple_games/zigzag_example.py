"""Zigzag Animation.

Creates a zigzag animation in the terminal using asterisks.
The pattern moves left and right across the screen continuously.

Features:
- Smooth animation with time delays
- Oscillating indent pattern (0 to 20 spaces)
- Keyboard interrupt handling for clean exit
"""

import time
import sys

indent = 0  # Current indentation level (number of spaces)
indentIncreasing = True  # Direction of movement (True = right, False = left)

try:
    while True:  # Main animation loop
        # Print the zigzag pattern with current indentation
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1)  # Pause for smooth animation (100ms)

        # Update indentation for next frame
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:  # Reached right edge
                indentIncreasing = False  # Start moving left
        else:
            indent = indent - 1
            if indent == 0:  # Reached left edge
                indentIncreasing = True  # Start moving right
except KeyboardInterrupt:
    # Allow clean exit with Ctrl+C
    sys.exit()
