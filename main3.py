x = float(input("Введіть значення x: "))

f = 0
k = 1
While True:
    if k > 7:
        f += (2 * (x + 1)**(3 - k)) / ((k + 1)**x + k**3)
        k += 1
    else:
        break

print("Значення f =", round(f, 3))