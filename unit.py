from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * (r ** 2)

radii = [2, 0, 2, -4]
for radius in radii:
    try:
        area = circle_area(radius)
        print(f"Radius: {radius}, Area: {area:.2f}")
    except ValueError as e:
        print(f"Radius: {radius}, Error: {e}")

