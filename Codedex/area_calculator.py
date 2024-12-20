
import math

print("=================")
print("Area Calculator")
print("=================")

print("\nChoose option:")
print("Square (A) \nRectangle (B) \nTriangle (C) \nCircle (D) \nQuit (E)") #Quadrat, Rechteck, Dreieck, Kreis
answer = input().capitalize()


while answer not in ["A", "B", "C", "D", "E"]:
    print("Wrong input!")
    answer = input().capitalize()
    

if answer == "A": #Square
    side = float(input("Please enter the side lenght in m: "))
    area = side ** 2
    print(f"The Square has an area of {area}m²")

elif answer == "B": #Rectangle
    lenght = float(input("Please enter the side lenght in m: "))
    width = float(input("Pleas enter now the width lenght in m: "))
    area = lenght * width
    print(f"The Rectangle has an are of{area}m²")

elif answer == "C": #Triangle
    base = float(input("Plase enter the base in m: "))
    height = float(input("Please enter now the height in m: "))
    area = base * height / 2
    print(f"The area of the triangle is {area}m²")

elif answer == "D": #Circle
    radius = float(input("Please enter your radius in m: "))
    area = radius * radius * math.pi
    print(f"The Circle has an area of {area}cm²")

else:
    quit()