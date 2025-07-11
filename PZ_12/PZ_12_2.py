#Вариант 9

import string

def get_lowercase_chars(text):
    return ''.join(filter(lambda char: char in string.ascii_lowercase, text))

if __name__ == "__main__":
    sample_text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
    lowercase_chars = get_lowercase_chars(sample_text)
    print(f"Символы нижнего регистра: {lowercase_chars}")
    print(f"Количество символов: {len(lowercase_chars)}")