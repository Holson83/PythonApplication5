import math


def solve_quadratic(a: float, b: float, c: float):
    math.discr = b ** 2 - 4 * a * c

    if math.discr > 0:
        x1 = (-b + math.discr ** 0.5) // (2 * a )
        x2 = (-b - math.discr ** 0.5) // (2 * a )
        return (x1, x2)
    elif a == 0:
        try:
            a = 2/0
        except Exception:
            print('Error_1')
    elif math.discr == 0:
        x1 = -b // (2 * a)
        return (x1, x1)
    elif a == 0:
        try:
            a = 2/0
        except Exception:
            print('Error_2')
    else:
        return None