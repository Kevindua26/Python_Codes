# Write a program to check collinearity using x,y coordinates.
print('Q86_CheckCollinearity.py')

def check_collinearity(x1, y1, x2, y2, x3, y3):
    """Check if three points are collinear using area formula"""
    # Area of triangle = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    # If area is 0, points are collinear
    return area == 0

# Get input from user
print("Enter coordinates of three points:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

# Check collinearity
if check_collinearity(x1, y1, x2, y2, x3, y3):
    print("\nThe points are COLLINEAR (lie on same line)")
else:
    print("\nThe points are NOT collinear")
