# Part A
text = "PythonProgramming"

#slice from start means starting from index 0 to a specified index

print("Slice from start (first 6):", text[:6])  # Output: Python

#slice to the end means starting from a specified index to the end of the string

print("Slice to end (from 6):", text[6:])      # Output: Programming



# Part B
def divide_if_floats(a, b, c=None, d=None):

    # Only param1 and param2 are used for division
    
    if isinstance(a, float) and isinstance(b, float):
        if b != 0:
            return int(a // b)
        else:
            return False
    else:
        return False


# Part C
tenants = []
MONTH_COST = 20000
TAX_RATE = 0.25
for i in range(5):
    print(f"\nEnter data for tenant {i+1}:")
    name = input("Tenant name: ")
    amount_paid = float(input("Amount paid: "))
    if amount_paid < MONTH_COST:
        print("Invalid amount. Must be at least one month's cost.")
        continue
    months_paid = int(amount_paid // (MONTH_COST + MONTH_COST * TAX_RATE))
    total_due = months_paid * (MONTH_COST + MONTH_COST * TAX_RATE)
    balance = amount_paid - total_due
    tenants.append((name, months_paid, balance))

print("\nTenants' months remaining and balances:")
for t in tenants:
    print(f"{t[0]}: Months paid = {t[1]}, Balance = {t[2]:.2f}")
