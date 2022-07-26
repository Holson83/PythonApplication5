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
    elif a == 0:
        try:
            if discr > 0:
                return None
            elif discr == 0:
                return None
        except ZeroDivisionError:
            a = 0
    elif b == 0:
        try:
            if discr > 0:
                x1 = (discr ** 0.5) / (2 * a)
                x2 = (discr ** 0.5) / (2 * a)
                return (x1, x2)
            elif discr == 0:
                x1 = 0
                return (x1, x1)
        except ZeroDivisionError:
            b = 0
    else:
        return None