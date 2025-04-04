try:

    a = float(input("Введите первое число: "))

    b = float(input("Введите второе число: "))

    result = a / b

    print(f"Результат деления: {result}")

except ZeroDivisionError:
    print("Делить на ноль нельзя")

except ValueError:

    print("Введите числовые значения")