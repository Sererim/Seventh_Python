from homework import fill_file
from homework import random_names
from homework import read_from_files

# 1.1
# - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
# - Первое число int, второе - float разделены вертикальной чертой. 
# - Минимальное число - -1000, максимальное - +1000. 
# - Количество строк и имя файла передаются как аргументы функции.

fill_file("test_dir/test_1.txt")

# 1.2
# - Напишите функцию, которая генерирует псевдоимена. 
# - Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. 
# - Полученные имена сохраните в файл

random_names()

# 1.3 
# - Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# - Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#     если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
#     если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# - В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# - При достижении конца более короткого файла, возвращайтесь в его начало.

read_from_files()

# 1.4
# - Создайте функцию, которая создаёт файлы с указанным расширением. 
# - Функция принимает следующие параметры:
#     расширение
#     минимальная длина случайно сгенерированного имени, по умолчанию 6
#     максимальная длина случайно сгенерированного имени, по умолчанию 30
#     минимальное число случайных байт, записанных в файл, по умолчанию 256
#     максимальное число случайных байт, записанных в файл, по умолчанию 4096
#     количество файлов, по умолчанию 42
#     Имя файла и его размер должны быть в рамках переданного диапазона.


