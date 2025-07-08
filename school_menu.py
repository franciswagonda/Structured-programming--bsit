# Campus Cafeteria Simple Ordering System

# Ask the student to enter the current hour

current_hour = int(input("Enter current hour (from 0 to 23): \n "))

# Check if the cafeteria is open (between 7:00 AM and 7:00 PM)

if current_hour < 7 or current_hour > 19:
    print("Cafeteria is closed. It is only open from 7:00 in the morning to 7:00 in the evening.")
else:
    print("\nWelcome to the Campus Cafeteria!")
    print("Menu:")
    print("1. Standard Meal - 12,000 Uganda Shillings")
    print("2. Vegetarian Meal - 10,000 Uganda Shillings")
    print("3. Deluxe Meal - 15,000 Uganda Shillings")

    # Ask the student to enter how many meals they want

    number_of_standard_meals = int(input("Enter number of Standard Meals: \n "))
    number_of_vegetarian_meals = int(input("Enter number of Vegetarian Meals: \n "))
    number_of_deluxe_meals = int(input("Enter number of Deluxe Meals: \n "))

    # Calculate total number of meals

    total_number_of_meals = number_of_standard_meals + number_of_vegetarian_meals + number_of_deluxe_meals

    # Calculate the total price

    total_price = (number_of_standard_meals * 12000) + (number_of_vegetarian_meals * 10000) + (number_of_deluxe_meals * 15000)

    # Apply discount if more than 3 meals are ordered

    if total_number_of_meals > 3:
        discount_amount = total_price * 0.10
        total_price = total_price - discount_amount
    else:
        discount_amount = 0

    # Show order summary
    print("\nOrder Summary:")
    print("Standard Meals:", number_of_standard_meals)
    print("Vegetarian Meals:", number_of_vegetarian_meals)
    print("Deluxe Meals:", number_of_deluxe_meals)
    print("Total number of meals:", total_number_of_meals)
    print("Discount given:", int(discount_amount), "Uganda Shillings")
    print("Total amount to pay:", int(total_price), "Uganda Shillings")
