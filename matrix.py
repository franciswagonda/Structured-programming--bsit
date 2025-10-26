import random
import time
import os
import sys

# ANSI color codes for green shades
colors = ["\033[92m", "\033[32m", "\033[38;5;46m"]

# Hide cursor
print("\033[?25l", end="")

# Get terminal size
cols = os.get_terminal_size().columns

# Create a list of positions for each column
drops = [0 for _ in range(cols)]

try:
    while True:
        # Slight delay for animation speed
        time.sleep(0.05)
        
        # Randomly print a character in each column
        for i in range(cols):
            if random.random() > 0.975:  # chance to reset a drop
                drops[i] = 0
            # Move cursor
            print(f"\033[{drops[i]};{i}H{random.choice(colors)}{random.choice('01abcdefghijklmnopqrstuvwxyz@$#%&*')}", end="")
            drops[i] += 1
        sys.stdout.flush()

except KeyboardInterrupt:
    # Reset terminal when user stops
    print("\033[0m\033[?25h")  # show cursor and reset colors
    print("\nMatrix rain stopped.")