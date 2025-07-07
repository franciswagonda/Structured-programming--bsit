
print("Input length and width")

def perimeter(l,w):
    return (l+w)*2

def area (l,w):
    return l*w 

l = float(input("length\n"))
w = float(input("width\n"))

print("Perimeter is", perimeter(l, w))  
print("Area is", area(l, w))
