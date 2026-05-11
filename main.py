import math

def main():
    try:
        # Ввід даних з клавіатури
        x = float(input("Введіть x: "))
        y = float(input("Введіть y: "))

        # Розрахунок аргументу логарифма
        # Оскільки логарифм від'ємного числа не існує, 
        # у таких завданнях зазвичай мається на увазі модуль або конкретні значення
        argument = math.pow(y, x) + x
        
        if argument <= 0:
            print("Помилка: Аргумент логарифма має бути більшим за нуль.")
            return

        # Обчислення функції f = ln(y^x + x) * (1 - 0.5y)
        f = math.log(argument) * (1 - 0.5 * y)

        print(f"Результат f: {f:.5f}")

    except ValueError:
        print("Помилка: Введіть числові значення.")
    except OverflowError:
        print("Помилка: Число занадто велике для обчислення.")

if __name__ == "__main__":
    main()
