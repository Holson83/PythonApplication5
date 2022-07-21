import math


print("Enter the coefficients for the equation")
print("ax^2 + bx2^2 + c(x2^2 + y1^2 - 2y1 * y2^2 - r^2) = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("D = %.2f" % discr)

if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
elif discr == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    print('There are no roots')
