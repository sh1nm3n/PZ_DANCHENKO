'''
Вариант 9.
Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
(путь), собственно имя и расширение. Выделить из этой строки имя файла (без
расширения).
'''
full_file_name = "C:/danch/PycharmProjects/IS-28/Proj_Danchenko/PZ_REPORTS/PZ_3.pdf"
file_name = full_file_name.split('/')[-1].split('.')[0]

print(file_name)
