import math


def solve_quadratic(a: float, b: float, c: float):
    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return (x1, x2)
    elif discr == 0:
        x1 = -b / (2 * a)
        return (x1, x1)
    else:
        return None