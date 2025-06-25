#Вариант 9.
with open('text18-9.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

lower_count = 0
for line in lines:
    print(line.strip())
    lower_count += sum(1 for char in line if char.islower())

print(f"\nКоличество букв в нижнем регистре: {lower_count}")

user_line = input("\nВведите строку для замены последней строки: ")
new_lines = lines[:-1] + [user_line + '\n']

with open('new_poem.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)