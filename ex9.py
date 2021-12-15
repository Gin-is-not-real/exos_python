import math

attendu1 = [-2.0, 1.0]
attendu2 = [-0.5]
attendu3 = []

def quadratic_equation(a, b, c):
    solutions = []

    DELTA = (b**2) - (4*(a*c))
    print('DELTA: ', DELTA)

    if DELTA == 0:
        x = (-b) / (2*a)
        solutions.append(x)

    if DELTA > 0:
        x1 = ( ((-b)-math.sqrt(DELTA)) / (2*a))
        x2 = ( ((-b)+math.sqrt(DELTA)) / (2*a))
        solutions.append(x1)
        solutions.append(x2)

    return solutions

# call
print(quadratic_equation(1, 1, -2))
print(quadratic_equation(4, 4, 1))
print(quadratic_equation(1, 1, 1))