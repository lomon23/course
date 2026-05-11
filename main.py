import math


x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

f = math.log(abs(y**x + x)) * (1 - 0.5 * y)


print("Значення функції f =", round(f, 3))

