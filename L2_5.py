# Создаём список чисел от 1 до 20
numbers = list(range(1, 21))

# Отфильтровываем чётные числа
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Увеличиваем каждое число на 10
increased_numbers = list(map(lambda x: x + 10, even_numbers))

# Сортируем по убыванию
sorted_numbers = sorted(increased_numbers, reverse=True)

# Выводим результат
print(f"Отфильтрованные чётные числа: {even_numbers}")
print(f"Числа, увеличенные на 10: {increased_numbers}")
print(f"Сортированные числа по убыванию: {sorted_numbers}")
