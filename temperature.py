

# Temperature scale program

print("Temperature scale")
temperature = float(input("Enter the temperature: "))
if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature < 15:
    print("Cold")
elif temperature >= 15 and temperature < 30:
    print("Moderate")
elif temperature >= 30 and temperature < 40:
    print("Hot")
elif temperature >= 40 and temperature < 50:
    print("Very Hot")                           
else:
    print("Extreme Hot")