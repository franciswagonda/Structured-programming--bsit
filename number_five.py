


print("Enter 5 numbers:")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

# Store in list
numbers = [a, b, c, d, e]

# Calculations
maximum = max(numbers)
minimum = min(numbers)
average = (a + b + c + d + e) / 5
sorted_list = sorted(numbers)

# Display
print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Sorted:", sorted_list)
