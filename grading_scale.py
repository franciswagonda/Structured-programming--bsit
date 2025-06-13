print("grading scale")
mark = int(input("mark between 100-0"))
if mark < 0 and mark > 100:
    print("invalid, Enter a valid mark") 
elif mark >=90 and mark <= 100:
    print("D1")
elif mark >=70 and mark <=89:
    print("D2")
elif mark >=65 and mark <=79:
    print("C3")
elif mark >=55 and mark <=64:
    print("C4")
elif mark >=50 and mark <=54:
    print("C5")
elif mark >=40 and mark <=49:
    print("C6")
elif mark >=35 and mark <=39:
    print("P7")
elif mark >=30 and mark <=34:
    print("P8")
else:
    print("F9")