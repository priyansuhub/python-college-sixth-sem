import math

def solve_quad(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("This equation has no real solutions.")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("This equation has one solution: ", x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("This equation has two solutions: ", x1, " and", x2)
solve_quad(1, -3, 2)