'''
using the python dictionary i created menu databases
'''

breakfast_menu = {
    1: ("Rolex", 5000),
    2: ("Katogo", 4000),
    3: ("Tea", 2000)
}

lunch_menu = {
    1: ("Posho & Beans", 7000),
    2: ("Matooke & Gnuts", 5500),
    3: ("Soda", 3000)
}


supper_menu = {
    1: ("Chips & Chicken", 7000),
    2: ("Pilau", 5500),
    3: ("Water", 1500)

}



'''
using a utility function to display the menu to the user
'''
def show_menu(menu):
    print("\nMenu:")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - UGX {price}")



'''
using a function to allow a user enter their order
'''
#used the

def take_order(menu):
    items = input("\nEnter item numbers (e.g. 1, 3):\n ").split(",")
    total = 0
    valid = False
    print("\nYour order is:")


#this checks in what the user enters and if the user enters the wrong input it will break instantly
    for item in items:
        item = item.strip()                                                                      #strip function helps separate the blocks of code used
        if item.isdigit():
            num = int(item)
            if num in menu:
                name, price = menu[num]
                print(f"- {name}: UGX {price}")
                total += price
                valid = True
            else:
                print(f"- Item {num} not found.")


    if valid:
        print("Ebenzer Restaurant")
        print(f"{name}")
        print(f"\nTotal: UGX {total}")
        
    else:
        print("No valid items selected.")

#used the while loop to keep the user in loop incase they select an option thats not among the required options
while True:
    print("\n Welcome to Ebenezer Restaurant!")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Supper")

    choice = input("Choose a meal (1,2 or 3): ")

    if choice == "1":
        show_menu(breakfast_menu)
        take_order(breakfast_menu)
        break

    elif choice == "2":
        show_menu(lunch_menu)
        take_order(lunch_menu)
        break
    
    elif choice =="3":
        show_menu(supper_menu)
        take_order(supper_menu)

        break
    else:

        print("Invalid choice. Try again.")



