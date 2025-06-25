#Вариант 9

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Более точное регулярное выражение
matches = re.findall(r'Достоевск[а-яё]+', text)
unique_matches = sorted(set(matches))

print("Найденные варианты фамилии Достоевского:")
for variant in unique_matches:
    print(variant)