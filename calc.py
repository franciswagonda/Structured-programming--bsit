
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))

print("Pick a calculation:\nAdd\nSubtract\nMultiply\nDivide")
         
calc = input()

if calc == 'Add':
    answer = num1 + num2

elif calc == 'Subtract':
    answer = num1 - num2
    
elif calc == 'Multiply':
    answer = num1 * num2
    
elif calc == 'Divide':
    answer = num1 / num2

print(answer)
    
