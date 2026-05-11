import math

def stvorennya_matrix(n, m):
    A = []

    for i in range(1, n + 1):
        ryadok = []
        for j in range(1, m + 1):
            a_ij = 1.5**(i + j) + math.cos(i * j) / ((i + j)**3)
            ryadok.append(a_ij)
        A.append(ryadok)
    return A

def stvorennya_vector(A, n, m):
    X = []
    for i in range(n):
        min_elem = A[i][0]
        max_elem = A[i][0]
        for j in range(m):
            if A[i][j] < min_elem:
                min_elem = A[i][j]
            if A[i][j] > max_elem:
                max_elem = A[i][j]
        X.append(min_elem + max_elem)
    return X

def vuvid_matrix(A, n, m):
    for i in range(n):
        for j in range(m):
            print(f"{A[i][j]:.3f}", end="\t")
        print()

def vuvid_vector(X):
    for i in range(len(X)):
        print(f"{X[i]:.3f}", end=" ")
    print()

n = 5
m = 5

A = stvorennya_matrix(n, m)
print("Матриця A:")
vuvid_matrix(A, n, m)

X = stvorennya_vector(A, n, m)
print("\nВектор X (сума max та min елементів рядків):")
vuvid_vector(X)