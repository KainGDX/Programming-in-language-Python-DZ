import random
with open("data.txt", "w") as file:

    for _ in range(10):

        file.write(f"{random.randint(1, 100)}\n")
with open("data.txt", "r") as file:

    numbers = [int(line.strip()) for line in file]
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
with open("result.txt", "w") as file:
    file.write(f"Сумма: {total}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум: {maximum}\n")
    file.write(f"Минимум: {minimum}\n")

print("Результаты сохранены в result.txt")