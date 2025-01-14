from math import pi

def circle_area(r):
    return pi*(r**2)
radii = [2,0,2,-4]
for radius in radii:
    area = circle_area(radius)
    print(f"Radius: {radius}, Area: {area}")

