import math

def f1(n, m):
    a = []
    for i in range(1, n + 1):
        r = []
        for j in range(1, m + 1):
            val = 1.5**(i+j) + math.cos(i*j) / ((i+j)**3)
            r.append(val)
        a.append(r)
    return a

def f2(a):
    x = []
    for r in a:
        mi = ma = r[0]
        for v in r:
            if v < mi: mi = v
            if v > ma: ma = v
        x.append(mi + ma)
    return x

def f3(a):
    for r in a:
        for v in r:
            print(f"{v:.3f}", end="\t")
        print()

def f4(x):
    for v in x:
        print(f"{v:.3f}", end=" ")
    print()

n = 5
m = 5

matr = f1(n, m)
print("Matrix A:")
f3(matr)

vec = f2(matr)
print("\nVector X:")
f4(vec)