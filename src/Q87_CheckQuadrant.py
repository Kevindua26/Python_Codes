# Write a program to check a point entered by the user lies in the first, second, third or fourth quadrant.

# Get coordinates from user
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Check quadrant
if x > 0 and y > 0:
    print(f"Point ({x}, {y}) lies in FIRST quadrant")
elif x < 0 and y > 0:
    print(f"Point ({x}, {y}) lies in SECOND quadrant")
elif x < 0 and y < 0:
    print(f"Point ({x}, {y}) lies in THIRD quadrant")
elif x > 0 and y < 0:
    print(f"Point ({x}, {y}) lies in FOURTH quadrant")
elif x == 0 and y == 0:
    print(f"Point ({x}, {y}) is at ORIGIN")
elif x == 0:
    print(f"Point ({x}, {y}) lies on Y-axis")
else:
    print(f"Point ({x}, {y}) lies on X-axis")

print('This code is written and executed by Kaivalaya Dua 0231BCA205')
