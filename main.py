from homework.seminar_first import fill_file
from homework.seminar_second import random_names
from homework.seminar_third import read_from_files
from homework.seminar_fourth import make_file
from homework.seminar_fith import make_extensions_files
from homework.seminar_sixth import make_files_in_directory
from homework.seminar_seventh import sort_files_by_extensions
from homework.home_task import mass_rename

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

make_file()

# 1.5 
# - Доработаем предыдущую задачу. 
# - Создайте новую функцию которая генерирует файлы с разными расширениями. 
# - Расширения и количество файлов функция принимает в качестве параметров. 
# - Количество переданных расширений может быть любым. 
# - Количество файлов для каждого расширения различно. 
# - Внутри используйте вызов функции из прошлой задачи.

make_extensions_files()

# 1.6
# - Дорабатываем функции из предыдущих задач. 
# - Генерируйте файлы в указанную директорию — отдельный параметр функции. 
# - Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
# - Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

make_files_in_directory()

# 1.7
# - Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# - Каждая группа включает файлы с несколькими расширениями. 
# - В исходной папке должны остаться только те файлы, которые не подошли для сортировки. 

sort_files_by_extensions()

# 2. Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# - К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 

