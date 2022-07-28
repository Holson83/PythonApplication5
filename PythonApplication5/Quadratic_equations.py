import math

def solve_linear(a: float, b: float): # a*x + b = 0
    return -b / a

def solve_quadratic(a: float, b: float, c: float): # a*x^2 + b*x + c = 0
    print(f'solve_quadratic({a}, {b}, {c})')
    try:
        print('try start')
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

    except ArithmeticError:
        print('ArithmeticError')
        return None

    finally:
        print('Finally')
