def check_triangle_type():
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))
    
    if side1 <= 10 and side2 <= 10 and side3 <= 10:
        # Check for Equilateral triangle
        if side1 == side2 == side3:
            print("This is an Equilateral triangle.")

        # Check for Isosceles triangle
        elif side1 == side2 or side2 == side3 or side1 == side3:
            print("This is an Isosceles triangle.")
            
        # If neither, it must be a Scalene triangle
        else:
            print("This is a Scalene triangle.")
    else:
        print("Enter sides less than or equal to 10.")

# Main program
check_triangle_type()
