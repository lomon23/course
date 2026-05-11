task1
```marmaid
graph TD
A([Початок]) --> B[/Ввід x, y/]
B --> C["f = ln(y^x + x) * (1 - 0.5y)"]
C --> D[/Вивід f/]
D --> E([Кінець])
```

task 2
```marmaid
graph TD
    A([Початок]) --> B[/Ввід x, a/]
    B --> C{x < 0?}
    C -- Так --> D["y = a * sin³(x)"]
    C -- Ні --> E{x <= 5?}
    E -- Так --> F["y = x * ∛(a*x³ + sin(x))"]
    E -- Ні --> G["y = log_x |x³ - eˣ|"]
    D --> H[/Вивід y/]
    F --> H
    G --> H
    H --> I([Кінець])
```


task 3

task4.1
```marmaid
graph TD
    A([Початок]) --> B[/Ввід x/]
    B --> C["f = 0
        k = 1"]
    C --> D{True?}
    D -- Так --> E{k > 7?}
    E -- Ні --> F[break]
    F --> G[/Вивід f/]
    G --> H([Кінець])
    E -- Так --> I["f = f + 2(x+1)³⁻ᵏ / ((k+1)ˣ + k³)"]
    I --> J["k = k + 1"]
    J --> D
```
task4.2
```marmaid
 graph TD
    subgraph stvorennya_vector
    A2([Початок підпрограми]) --> B2["X = []"]
    B2 --> C2{"i = 0 .. n-1"}
    C2 -- Так --> D2["min_elem = A[i][0]<br>max_elem = A[i][0]"]
    D2 --> E2{"j = 0 .. m-1"}
    E2 -- Так --> F2{"A[i][j] < min_elem?"}
    F2 -- Так --> G2["min_elem = A[i][j]"]
    F2 -- Ні --> H2{"A[i][j] > max_elem?"}
    G2 --> H2
    H2 -- Так --> I2["max_elem = A[i][j]"]
    H2 -- Ні --> J2["Наступний j"]
    I2 --> J2
    J2 --> E2
    E2 -- Ні --> K2["X.append(min_elem + max_elem)"]
    K2 --> C2
    C2 -- Ні --> L2["return X"]
    L2 -> M2([Кінець підпрограми])
    end 
```

task5.1
```marmaid
graph TD
    A([Початок: calculate_matrix]) --> B[Створити порожній список matrix]
    B --> C{Цикл i від 1 до 5}
    C -- Так --> D[Створити порожній список row]
    D --> E{Цикл j від 1 до 5}
    E -- Так --> F["val = 1.5^(i+j) + cos(i*j) / (i+j)^3"]
    F --> G[Додати val у row]
    G --> E
    E -- Ні --> H[Додати row у matrix]
    H --> C
    C -- Ні --> I([Кінець: повернути matrix])
```
task5.2
```marmaid
graph TD
    A([Початок: calculate_vector]) --> B[Створити порожній список vector]
    B --> C{Для кожного рядка row у matrix}
    C -- Так --> D["Знайти max(row) та min(row)"]
    D --> E["xi = max + min"]
    E --> F[Додати xi у vector]
    F --> C
    C -- Ні --> G([Кінець: повернути vector])
```
task5.3
```marmaid
graph TD
    A([Початок: print_matrix]) --> B{Для кожного рядка у matrix}
    B -- Так --> C[Вивести всі елементи рядка]
    C --> B
    B -- Ні --> D([Кінець])
```
