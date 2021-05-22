import math  # Import pi from math module


def area():
    radius = float(input("Enter radius of circle: "))  # Accept radius from user
    area_circle = math.pi * radius * radius  # Calculate
    print(f'Area of circle of radius {radius} = {area_circle}')  # Display output
