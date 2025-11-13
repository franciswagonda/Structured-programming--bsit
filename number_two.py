##Question Two (10 Marks)
"""
With the use of If statements, write a python program that allows an instructor to enter a mark strictly
between 0 and 100. On receiving the mark, the program has to assign a grade based on your defined
clusters ie 80-90 is A, 91 -100 is A+ etc. When a negative mark is entered, the program should not stop
but prompt the user to enter a valid mark.
"""


print("Enter students marks")
mark = float(input("Enter a mark between 0 and 100: "))
if mark < 0 or mark > 100:
  print("Enter a valid mark")
elif mark >= 91 and mark <= 100:
  print("Grade A+")
elif mark >= 80 and mark < 91:
  print("Grade A")
elif mark >= 70 and mark < 80:
  print("Grade B")
elif mark >= 60 and mark < 70:
  print("Grade C")
elif mark >= 50 and mark < 60:
 print("Grade D")

