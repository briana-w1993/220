import math
a, b, c = eval(input("enter coefficients a, b, and c: "))
sqrt_discr = math.sqrt(b * b - 4 * a * c)
denom = 2 * a
root_1 = (-b + sqrt_discr) / denom
root_2 = (-b + sqrt_discr) / denom
print("root 1:", root_1, "root 2:", root_2)