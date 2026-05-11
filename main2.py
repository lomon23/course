import math

x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))

if x < 0:
    y = a * (math.sin(x) ** 3)
elif x <= 5:
    y = x * math.cbrt(a * (x**3) + math.sin(x))
else:
    y = math.log(abs(x**3 - math.exp(x)), x)

print("Значення функції y =", round(y, 3))