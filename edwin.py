print("choose options 1, 2 or 3 ")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area and perimeter of a rectangle")
print("4.area and perimeter of asquare")
choice=int(input("choose among the choices :"))

from math import pi
if choice ==1:
          #input the radius
          radius=float(input("Enter radius of the circle"))
          #calculate the area
          area=float(pi*radius*radius)
          #calculate the circumference
          circumference=float(2*pi*radius)
          #output the area and the circumference
          print(" area of circle " ,area)
          print("circumference of circle",circumference)
elif choice ==2:
          #input the base, height and the hypoteneus of the triangle
        base=float(input("Enter base of the triangle"))
        height=float(input("Enter the height of the triangle"))
        hypotenuse=float(input("Enter the hypotenuse of the circle"))
          #calculate the area
        area=float(0.5*base*height)
          #calculate the perimeter
        perimeter=(base+hypotenuse+hypotenuse)
          #output the area and the perimeter of the triangle
        print("area of triangle",area)
        print("perimeter of triangle",perimeter)
elif choice ==3:
          #input the length and width of the rectangle
        width=float(input("Enter the width of the rectangle"))
        length=float(input("Enter the length of the rectangle"))
          #calculate the area
        area=float(length*width)
          #calculate the perimeter of the rectangle
        perimeter=2(length+width)
          #output the area and the perimeter of the rectangle
        print("area of rectangle",area)
        print("perimeter of rectangle",perimeter)
elif choice==4:
          #input the side (s)
def calculate_perimeter(side):
    # Perimeter of the square
    perimeter = 4 * side
    return perimeter

def calculate_area(side):
    # Area of the square
    area = side ** 2
    return area

# Input the side of the square
side = float(input("Enter the side length of the square: "))

# Calculate the perimeter
perimeter = calculate_perimeter(side)

# Calculate the area
area = calculate_area(side)

# Display the results
print(f"The perimeter of the square is: {perimeter}")
print(f"The area of the square is: {area}")


else:
        print("invalid option choose 1,2,3 or 4")
    
