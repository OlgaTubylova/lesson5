# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path: str):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

# Пример использования
file_path = "/home/user/documents/example.txt"
result = split_file_path(file_path)
print(f"Путь: {result[0]}\nИмя файла: {result[1]}\nРасширение файла: {result[2]}")