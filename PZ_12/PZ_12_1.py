#Вариант 9

def find_common_elements(seq1, seq2):
    common = set(filter(lambda x: x in seq2, seq1))
    return common, len(common)


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]

    common_elements, count = find_common_elements(list1, list2)
    print(f"Общие элементы: {common_elements}")
    print(f"Количество общих элементов: {count}")