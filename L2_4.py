import re

with open('text.txt', 'r') as file:
    text = file.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)
capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', text)

with open('emails.txt', 'w') as file:
    file.write("\n".join(emails))
with open('phones.txt', 'w') as file:
    file.write("\n".join(phones))
with open('capital_words.txt', 'w') as file:
    file.write("\n".join(capital_words))

print(f"Результаты сохранены в файлы.")
